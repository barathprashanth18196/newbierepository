"""TOPSIS, AHP consistency, and weight-sensitivity analysis for the 2026 fellowship rank list."""
import math

CRITERIA = ["Teaching/Research", "Field Preference", "Geography", "Culture"]
WEIGHTS = [0.35, 0.30, 0.175, 0.175]

# name: (Teaching/Research, Field Preference, Geography, Culture)
PROGRAMS = {
    "MCW": (10, 6.67, 8, 10),
    "Henry Ford": (6, 10, 10, 10),
    "LSU": (10, 10, 2, 10),
    "MCG": (10, 10, 0, 5),
    "Tufts": (10, 0, 6, 10),
    "UMass Chan": (8, 0, 6, 10),
    "NGMC": (4, 6.67, 4, 5),
    "ETSU": (8, 3.33, 0, 0),
    "Ann Arbor": (0, 0, 10, 10),
    "Wayne State": (2, 0, 10, 0),
}


def weighted_sum(weights):
    return {p: sum(w * x for w, x in zip(weights, v)) for p, v in PROGRAMS.items()}


def ranks(scores, eps=1e-9):
    """Competition ranking (ties share the best rank)."""
    return {p: 1 + sum(1 for q in scores if scores[q] > scores[p] + eps) for p in scores}


def topsis(weights):
    names = list(PROGRAMS)
    m = [PROGRAMS[n] for n in names]
    norms = [math.sqrt(sum(r[j] ** 2 for r in m)) for j in range(4)]
    v = [[weights[j] * r[j] / norms[j] for j in range(4)] for r in m]
    best = [max(r[j] for r in v) for j in range(4)]
    worst = [min(r[j] for r in v) for j in range(4)]
    out = {}
    for n, r in zip(names, v):
        dp = math.sqrt(sum((r[j] - best[j]) ** 2 for j in range(4)))
        dm = math.sqrt(sum((r[j] - worst[j]) ** 2 for j in range(4)))
        out[n] = (dp, dm, dm / (dp + dm))
    return out


def ahp(matrix):
    n = len(matrix)
    # Principal eigenvector by power iteration
    w = [1 / n] * n
    for _ in range(1000):
        nw = [sum(matrix[i][j] * w[j] for j in range(n)) for i in range(n)]
        s = sum(nw)
        nw = [x / s for x in nw]
        if max(abs(a - b) for a, b in zip(nw, w)) < 1e-14:
            w = nw
            break
        w = nw
    aw = [sum(matrix[i][j] * w[j] for j in range(n)) for i in range(n)]
    lam = sum(aw[i] / w[i] for i in range(n)) / n
    ci = (lam - n) / (n - 1)
    ri = {3: 0.58, 4: 0.90, 5: 1.12}[n]
    return w, lam, ci, ci / ri


def perturb(i, factor):
    w = list(WEIGHTS)
    new = w[i] * factor
    rest = 1 - w[i]
    return [new if j == i else w[j] * (1 - new) / rest for j in range(4)]


if __name__ == "__main__":
    base = weighted_sum(WEIGHTS)
    base_r = ranks(base)
    print("== Baseline weighted sum ==")
    for p in sorted(base, key=lambda p: -base[p]):
        print(f"{base_r[p]:>2} {p:<12} {base[p]:.4f}")

    print("\n== TOPSIS ==")
    t = topsis(WEIGHTS)
    tc = {p: t[p][2] for p in t}
    tr = ranks(tc)
    for p in sorted(tc, key=lambda p: -tc[p]):
        print(f"{tr[p]:>2} {p:<12} D+={t[p][0]:.4f} D-={t[p][1]:.4f} C={tc[p]:.4f}  (WS rank {base_r[p]})")

    print("\n== AHP ==")
    # Implied ratio matrix (exactly consistent) and a Saaty-scale version
    exact = [[WEIGHTS[i] / WEIGHTS[j] for j in range(4)] for i in range(4)]
    w, lam, ci, cr = ahp(exact)
    print("Exact ratios: w=", [round(x, 4) for x in w], f"lmax={lam:.4f} CI={ci:.4f} CR={cr:.4f}")
    # Saaty integer judgments, as a person would give them
    saaty = [
        [1, 1, 2, 2],
        [1, 1, 2, 2],
        [1 / 2, 1 / 2, 1, 1],
        [1 / 2, 1 / 2, 1, 1],
    ]
    w, lam, ci, cr = ahp(saaty)
    print("Saaty (T=F):  w=", [round(x, 4) for x in w], f"lmax={lam:.4f} CI={ci:.4f} CR={cr:.4f}")
    saaty2 = [
        [1, 2, 2, 2],
        [1 / 2, 1, 2, 2],
        [1 / 2, 1 / 2, 1, 1],
        [1 / 2, 1 / 2, 1, 1],
    ]
    w, lam, ci, cr = ahp(saaty2)
    print("Saaty (T=2F): w=", [round(x, 4) for x in w], f"lmax={lam:.4f} CI={ci:.4f} CR={cr:.4f}")

    print("\n== Sensitivity (+/-10%, one at a time, others renormalized) ==")
    all_ranks = {p: [] for p in PROGRAMS}
    for i, c in enumerate(CRITERIA):
        for f in (0.9, 1.1):
            w = perturb(i, f)
            s = weighted_sum(w)
            r = ranks(s)
            label = f"{c} {'-' if f < 1 else '+'}10%"
            print(f"\n{label}: weights={[round(x, 4) for x in w]}")
            for p in sorted(s, key=lambda p: -s[p])[:5]:
                print(f"   {r[p]:>2} {p:<12} {s[p]:.4f}")
            print(f"   HF-LSU gap = {s['Henry Ford'] - s['LSU']:+.4f}; MCW-next gap = {s['MCW'] - max(v for k, v in s.items() if k != 'MCW'):+.4f}")
            for p in PROGRAMS:
                all_ranks[p].append(r[p])
    print("\nRank range per program (baseline + 8 scenarios):")
    for p in sorted(PROGRAMS, key=lambda p: base_r[p]):
        rs = [base_r[p]] + all_ranks[p]
        print(f"   {p:<12} base {base_r[p]}  min {min(rs)} max {max(rs)}  all={all_ranks[p]}")
