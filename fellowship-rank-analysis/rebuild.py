"""Rebuilt rank formula (2026-09-29): AHP-derived weights, Culture as a composite."""
import analysis
from analysis import ahp, ranks

CRITERIA = ["Teaching/Research", "Field Preference", "Geography", "Culture"]
# Barath's pairwise judgments, 2026-09-29 (row criterion vs column criterion)
PAIRWISE = [
    [1, 2, 5, 5],          # Teaching: a bit more than Field, much more than Geography and Culture
    [1 / 2, 1, 2, 2],      # Field: a bit more than Geography and Culture
    [1 / 5, 1 / 2, 1, 2],  # Geography: a bit more than Culture
    [1 / 5, 1 / 2, 1 / 2, 1],
]
WEIGHTS = [0.532, 0.237, 0.136, 0.095]  # AHP eigenvector rounded to 3 dp, sums to 1

# Culture sub-weights: interview read, 24-hour call, leave (>=20 days), moonlighting
CULTURE_WEIGHTS = (0.5, 0.2, 0.2, 0.1)
NEUTRAL = 5  # not yet interviewed / unknown

# name: Teaching, Field, Geography, interview read (None = not interviewed),
#       24h call (1 favorable / 0 unfavorable / None unknown), vacation days, moonlighting
PROGRAMS = {
    "MCW": (10, 6.67, 8, 10, 1, 15, "No"),
    "Henry Ford Providence": (6, 10, 10, None, None, 20, "TBD"),
    "LSU New Orleans": (10, 10, 2, None, 0, 28, "TBD"),
    "MCG": (10, 10, 0, 5, 0, 21, "Yes"),
    "Tufts": (10, 0, 6, None, None, 20, "TBD"),
    "UMass Chan": (8, 0, 6, None, None, 20, "TBD"),
    "NGMC": (4, 6.67, 4, None, None, 15, "No"),
    "ETSU": (8, 3.33, 0, 0, None, 15, "No"),
    "Ann Arbor": (0, 0, 10, 10, None, 28, "TBD"),
    "Wayne State": (2, 0, 10, None, None, 21, "TBD"),
}


def culture(read, call, vacation, moonlighting):
    parts = (
        NEUTRAL if read is None else read,
        NEUTRAL if call is None else 10 * call,
        10 if vacation >= 20 else 0,
        {"Yes": 10, "No": 0}.get(moonlighting, NEUTRAL),
    )
    return sum(w * p for w, p in zip(CULTURE_WEIGHTS, parts))


def matrix():
    return {n: (t, f, g, round(culture(*rest), 4)) for n, (t, f, g, *rest) in PROGRAMS.items()}


if __name__ == "__main__":
    w, lam, ci, cr = ahp(PAIRWISE)
    print("AHP weights", [round(x, 4) for x in w], f"lmax={lam:.4f} CR={cr:.4f}")
    m = matrix()
    score = {n: sum(a * b for a, b in zip(WEIGHTS, v)) for n, v in m.items()}
    r = ranks(score)
    analysis.PROGRAMS = m
    t = analysis.topsis(WEIGHTS)
    tr = ranks({n: t[n][2] for n in t})
    for n in sorted(score, key=lambda n: -score[n]):
        print(f"{r[n]:>2} {n:<22} {score[n]:.3f}  T={m[n][0]:<5} F={m[n][1]:<5} G={m[n][2]:<3} C={m[n][3]:<5} TOPSIS#{tr[n]} C*={t[n][2]:.4f}")
    # sensitivity: +/-10% per weight
    analysis.WEIGHTS = WEIGHTS
    moves = {n: set([r[n]]) for n in m}
    for i in range(4):
        for f in (0.9, 1.1):
            s = analysis.weighted_sum(analysis.perturb(i, f))
            for n, k in ranks(s).items():
                moves[n].add(k)
    print("rank range under +/-10%:", {n: (min(v), max(v)) for n, v in moves.items()})
