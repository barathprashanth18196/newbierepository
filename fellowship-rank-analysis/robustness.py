"""Standard robustness report for the rank list. Run after every rescore: python3 robustness.py

1. One-at-a-time weight sensitivity (+/-10% and +/-20%)
2. Weight stability: smallest single-weight change that flips each adjacent pair
3. Teaching break-even: clinical or research points needed to pass the program above
4. Pending inputs: best/worst-case rank for every program with unknowns
5. Leave-one-criterion-out
6. Alternative methods: equal weights, rank-order-centroid weights, weighted product, TOPSIS
7. Monte Carlo (montecarlo.py, scenarios A and B)
8. Gut check: model rank vs Barath's own "My Rank" column (Spearman)
"""
import analysis
import montecarlo
import rebuild as r

NAMES = ["Teaching", "Field", "Geography", "Culture"]
W = r.WEIGHTS
# Barath's gut "My Rank" column from Notion, read 2026-10-06. Refresh from Notion before each run.
# Barath 2026-10-06: My Rank is out of date. Check 8 is skipped until he writes a fresh gut order
# (planned for the blind re-scoring after the last interview); then set MY_RANK_CURRENT = True.
MY_RANK_CURRENT = False
MY_RANK = {
    "Henry Ford Providence": 1, "Tufts": 2, "UMass Chan": 3, "MCG": 4, "ETSU": 5,
    "MCW": 6, "NGMC": 7, "LSU New Orleans": 8, "Ann Arbor": 9, "Wayne State": 10,
}


def scores(m, w=W):
    return {n: sum(a * b for a, b in zip(w, v)) for n, v in m.items()}


def order(m, w=W):
    return r.final_order(scores(m, w), m)


def rank_of(m, w=W):
    return {n: i for i, n in enumerate(order(m, w), 1)}


def reweight(i, new):
    """Set weight i to `new`, scaling the others proportionally so they still sum to 1."""
    k = (1 - new) / (1 - W[i])
    return [new if j == i else x * k for j, x in enumerate(W)]


def matrix_with(overrides):
    progs = dict(r.PROGRAMS)
    progs.update(overrides)
    return {
        n: (r.teaching(n, c), f, g, r.culture(*rest, emr_good=n not in r.BAD_EMR))
        for n, (c, f, g, *rest) in progs.items()
    }


def fmt_range(lo, hi):
    return f"{lo}" if lo == hi else f"{lo}-{hi}"


def main():
    m = r.matrix()
    base = order(m)
    s = scores(m)
    base_rank = {n: i for i, n in enumerate(base, 1)}

    print("BASE ORDER")
    for i, n in enumerate(base, 1):
        print(f"{i:>2} {n:<22} {s[n]:.3f}")

    print("\n1. ONE-AT-A-TIME WEIGHT SENSITIVITY (others rescaled to sum to 1)")
    for pct in (0.10, 0.20):
        rng = {n: [base_rank[n]] * 2 for n in m}
        for i in range(4):
            for f in (1 - pct, 1 + pct):
                for n, k in rank_of(m, reweight(i, W[i] * f)).items():
                    rng[n] = [min(rng[n][0], k), max(rng[n][1], k)]
        moved = {n: fmt_range(*v) for n, v in rng.items() if v[0] != v[1]}
        print(f"  +/-{pct:.0%}: programs that can move -> {moved or 'none'}")

    print("\n2. WEIGHT STABILITY: smallest single-weight change that flips each adjacent pair")
    print("   (relative change to that weight; >50% = solid, <10% = fragile)")
    for a, b in zip(base, base[1:]):
        best = None
        for i in range(4):
            for step in range(1, 1001):
                for sign in (1, -1):
                    new = W[i] * (1 + sign * step / 1000 * 3)  # scan up to +/-300%
                    if not 0 <= new < 1:
                        continue
                    k = rank_of(m, reweight(i, new))
                    if k[b] < k[a]:
                        cand = (step * 3 / 1000, NAMES[i], "up" if sign > 0 else "down")
                        best = cand if best is None or cand[0] < best[0] else best
                        break
                else:
                    continue
                break
        if best:
            tag = "FRAGILE" if best[0] < 0.10 else ("solid" if best[0] > 0.5 else "")
            print(f"  {a} > {b}: flips if {best[1]} weight goes {best[2]} {best[0]:.0%} {tag}")
        else:
            print(f"  {a} > {b}: no single-weight change flips it")

    print("\n3. TEACHING BREAK-EVEN: points needed to pass the program directly above")
    print("   (clinical carries 65% of Teaching, research 35%)")
    for above, n in zip(base, base[1:]):
        need = (s[above] - s[n]) / W[0]
        print(f"  {n:<22} needs +{need / r.TEACHING_SPLIT[0]:.2f} clinical or "
              f"+{need / r.TEACHING_SPLIT[1]:.2f} research to pass {above}")

    print("\n4. PENDING INPUTS: rank if every unknown resolves best vs worst (others held at base)")
    for n, (t, f, g, read, call, vac, moon) in r.PROGRAMS.items():
        unknown = [x for x, u in (("read", read is None), ("call", call is None), ("moonlighting", moon == "TBD")) if u]
        if not unknown:
            continue
        out = []
        for label, rd, cl, mn in (("best", 10, 1, "Yes"), ("worst", 0, 0, "No")):
            mm = matrix_with({n: (t, f, g, rd if read is None else read,
                                  cl if call is None else call, vac,
                                  mn if moon == "TBD" else moon)})
            out.append(f"{label} #{rank_of(mm)[n]} ({scores(mm)[n]:.3f})")
        print(f"  {n:<22} now #{base_rank[n]}; pending {', '.join(unknown)} -> {'; '.join(out)}")

    print("\n5. LEAVE-ONE-CRITERION-OUT (that weight set to 0, others rescaled)")
    for i in range(4):
        k = rank_of(m, reweight(i, 0))
        moved = [f"{n} {base_rank[n]}->{k[n]}" for n in base if k[n] != base_rank[n]]
        print(f"  without {NAMES[i]:<9}: top 3 = {', '.join(order(m, reweight(i, 0))[:3])}; moves: {', '.join(moved) or 'none'}")

    print("\n6. ALTERNATIVE METHODS (rank per program)")
    analysis.PROGRAMS = m
    t = analysis.topsis(W)
    alt = {
        "Equal weights": rank_of(m, [0.25] * 4),
        "Rank-order centroid": rank_of(m, [0.521, 0.271, 0.146, 0.062]),
        "Weighted product": analysis.ranks({n: _wpm(v) for n, v in m.items()}),
        "TOPSIS": analysis.ranks({n: t[n][2] for n in t}),
    }
    print(f"  {'Program':<22} {'Model':>5} " + " ".join(f"{k[:12]:>12}" for k in alt))
    for n in base:
        print(f"  {n:<22} {base_rank[n]:>5} " + " ".join(f"{alt[k][n]:>12}" for k in alt))

    print("\n7. MONTE CARLO")
    montecarlo.random.seed(2026)
    montecarlo.report("A. Weight uncertainty + unknown inputs", montecarlo.simulate(False))
    montecarlo.report("B. Same + +/-1 tier noise on clinical and research", montecarlo.simulate(True))

    print("\n8. GUT CHECK vs 'My Rank' (Notion)")
    if not MY_RANK_CURRENT:
        print("  skipped: My Rank is out of date (Barath, 2026-10-06). Refresh it at the blind re-scoring.")
        return
    rho = spearman(base_rank, MY_RANK)
    print(f"  Spearman rho = {rho:.2f} (1 = identical order, 0 = unrelated)")
    gaps = sorted(base, key=lambda n: -abs(base_rank[n] - MY_RANK[n]))
    for n in gaps:
        d = MY_RANK[n] - base_rank[n]
        if abs(d) >= 3:
            print(f"  {n:<22} model #{base_rank[n]} vs gut #{MY_RANK[n]}  (gap {abs(d)}) <- discuss")


def _wpm(v):
    p = 1.0
    for w, x in zip(W, v):
        p *= max(x, 0.5) ** w  # floor at 0.5 so a single 0 doesn't zero the product
    return p


def spearman(a, b):
    n = len(a)
    return 1 - 6 * sum((a[k] - b[k]) ** 2 for k in a) / (n * (n * n - 1))


if __name__ == "__main__":
    main()
