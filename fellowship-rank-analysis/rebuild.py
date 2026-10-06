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

# Culture sub-weights: interview read, 24-hour call, leave (>=20 days), moonlighting, EMR.
# 2026-10-06: Barath removed leave and EMR from Culture; the other three were rescaled
# proportionally (45/18/9 -> 62.5/25/12.5). Leave and EMR stay as reference data only.
CULTURE_WEIGHTS = (0.625, 0.25, 0.0, 0.125, 0.0)
BAD_EMR = {"Wayne State"}  # Cerner/Oracle Health; every other program runs Epic

# Only genuinely tied scores (equal at the 3 decimals shown) go to the tiebreak:
# Geography, then Field Preference,
# then familiarity (NGMC is Barath's home program).
TIE_BAND = 0.0005  # Barath 2026-10-02: tiebreak applies only to actual ties, not near-ties
HOME_PROGRAM = "NGMC"
NEUTRAL = 5  # not yet interviewed / unknown

# Confirmed with Barath program by program, 2026-09-29.
# name: Teaching, Field, Geography, interview read (None = not interviewed),
#       24h call (1 favorable / 0 unfavorable / None unknown), vacation days, moonlighting
# Geography (2026-10-04, 5 tiers evenly spaced): Michigan 10 > Boston area 7.5 >
#   Milwaukee = Gainesville 5 > New Orleans 2.5 > Augusta, Johnson City 0
# Field tiers: Heme/Onc 10 > CCM/PCCM 7.5 > ID/CCM combined 5 > ID + optional CCM 2.5 > plain ID 0
PROGRAMS = {
    "MCW": (8, 7.5, 5, 10, 1, 15, "No"),
    "Henry Ford Providence": (4, 10, 10, 2.5, 0, 20, "No"),
    "LSU New Orleans": (8, 10, 2.5, 7.5, 0, 28, "TBD"),
    "MCG": (8, 10, 0, 7.5, 0, 21, "Yes"),
    "Tufts": (10, 2.5, 7.5, 10, 1, 20, "No"),
    "UMass Chan": (8, 0, 7.5, None, None, 20, "TBD"),
    "NGMC": (4, 7.5, 5, 7.5, 0, 15, "No"),
    "ETSU": (6, 5, 0, 7.5, None, 15, "TBD"),
    "Ann Arbor": (4, 0, 10, 5, 1, 28, "No"),
    "Wayne State": (6, 0, 10, None, None, 21, "TBD"),
}


def culture(read, call, vacation, moonlighting, emr_good=True):
    parts = (
        NEUTRAL if read is None else read,
        NEUTRAL if call is None else 10 * call,
        10 if vacation >= 20 else 0,
        {"Yes": 10, "No": 0}.get(moonlighting, NEUTRAL),
        10 if emr_good else 0,
    )
    return sum(w * p for w, p in zip(CULTURE_WEIGHTS, parts))


def matrix():
    return {
        n: (t, f, g, round(culture(*rest, emr_good=n not in BAD_EMR), 4))
        for n, (t, f, g, *rest) in PROGRAMS.items()
    }


def final_order(score, m):
    """Sort by score; adjacent programs within TIE_BAND are ordered by the tiebreak chain."""
    order = sorted(score, key=lambda n: -score[n])
    key = lambda n: (m[n][2], m[n][1], n == HOME_PROGRAM)
    changed = True
    while changed:
        changed = False
        for i in range(len(order) - 1):
            a, b = order[i], order[i + 1]
            if abs(score[a] - score[b]) < TIE_BAND and key(b) > key(a):
                order[i], order[i + 1] = b, a
                changed = True
    return order


if __name__ == "__main__":
    w, lam, ci, cr = ahp(PAIRWISE)
    print("AHP weights", [round(x, 4) for x in w], f"lmax={lam:.4f} CR={cr:.4f}")
    m = matrix()
    score = {n: sum(a * b for a, b in zip(WEIGHTS, v)) for n, v in m.items()}
    r = ranks(score)
    analysis.PROGRAMS = m
    t = analysis.topsis(WEIGHTS)
    tr = ranks({n: t[n][2] for n in t})
    for i, n in enumerate(final_order(score, m), 1):
        print(f"{i:>2} (raw {r[n]}) {n:<22} {score[n]:.3f}  T={m[n][0]:<5} F={m[n][1]:<5} G={m[n][2]:<3} C={m[n][3]:<5} TOPSIS#{tr[n]} C*={t[n][2]:.4f}")
    # sensitivity: +/-10% per weight
    analysis.WEIGHTS = WEIGHTS
    moves = {n: set([r[n]]) for n in m}
    for i in range(4):
        for f in (0.9, 1.1):
            s = analysis.weighted_sum(analysis.perturb(i, f))
            for n, k in ranks(s).items():
                moves[n].add(k)
    print("rank range under +/-10%:", {n: (min(v), max(v)) for n, v in moves.items()})
