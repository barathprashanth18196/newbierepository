"""Rebuilt rank formula (2026-09-29): AHP-derived weights, Culture as a composite."""
import analysis
from analysis import ahp, ranks

CRITERIA = ["Teaching/Research", "Field Preference", "Geography", "Culture"]
# Barath's pairwise judgments, 2026-09-29 (row criterion vs column criterion).
# 2026-10-09: Field vs Geography changed from "Field a bit more" (2) to equal (1), so Geography
# gains weight and Field loses some (Barath: "a little bit more geography, a little bit less field").
PAIRWISE = [
    [1, 2, 5, 5],          # Teaching: a bit more than Field, much more than Geography and Culture
    [1 / 2, 1, 1, 2],      # Field: equal to Geography, a bit more than Culture
    [1 / 5, 1, 1, 2],      # Geography: a bit more than Culture
    [1 / 5, 1 / 2, 1 / 2, 1],
]
WEIGHTS = [0.544, 0.201, 0.161, 0.094]  # AHP eigenvector rounded to 3 dp, sums to 1 (CR 0.032)

# Teaching/Research composite (2026-10-09): 65% clinical + 35% research, both on 0-10.
# Clinical = Barath's original Teaching scores (4/6/8/10), spread evenly to 0-10 (0/3.33/6.67/10).
# Research: Barath's 5-tier order, evenly spaced 0-10.
TEACHING_SPLIT = (0.65, 0.35)
RESEARCH = {
    "Tufts": 10,                                    # maximum
    "MCG": 7.5,                                     # second top
    "UMass Chan": 5,                                # one step below MCG
    "MCW": 2.5, "LSU New Orleans": 2.5, "NGMC": 2.5, "Ann Arbor": 2.5,  # one step above lowest
    "Henry Ford Providence": 0, "ETSU": 0, "Wayne State": 0,          # lowest
}

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
# name: Clinical, Field, Geography, interview read (None = not interviewed),
#       24h call (1 favorable / 0 unfavorable / None unknown), vacation days, moonlighting
# Clinical (2026-10-09, 4 tiers evenly spaced from Barath's 10/8/6/4): 10 / 6.67 / 3.33 / 0
# Geography (2026-10-04, 5 tiers evenly spaced): Michigan 10 > Boston area 7.5 >
#   Milwaukee = Gainesville 5 > New Orleans 2.5 > Augusta, Johnson City 0
# Field tiers (2026-10-07, 4 tiers evenly spaced): Heme/Onc 10 > CCM / PCCM / ID-CCM combined 6.67
#   > ID + optional CCM 3.33 > plain ID 0
PROGRAMS = {
    "MCW": (6.67, 6.67, 5, 7.5, 1, 15, "No"),  # clinical 8; 10/7: PD not liked
    "Henry Ford Providence": (0, 10, 10, 2.5, 0, 20, "No"),  # clinical 4
    "LSU New Orleans": (3.33, 10, 2.5, 5, 0, 28, "No"),  # clinical 6 (10/9: "same as ETSU", was 8). 10/7: PD not liked; coordinator not liked (faculty, fellows). 10/9: moonlighting No (manual: J-1 may not moonlight)
    "MCG": (6.67, 10, 0, 6.25, 0, 21, "Yes"),  # clinical 8; 10/7: PD not liked (fellows, coordinator, faculty half)
    "Tufts": (10, 3.33, 7.5, 10, 1, 20, "No"),  # clinical 10
    "UMass Chan": (6.67, 0, 7.5, None, None, 20, "TBD"),  # clinical 8
    "NGMC": (0, 6.67, 5, 8.75, 0, 15, "No"),  # clinical 4; 10/6: no fellows yet (first cohort), fellows item neutral 1.25
    "ETSU": (3.33, 6.67, 0, 7.5, None, 15, "TBD"),  # clinical 6
    "Ann Arbor": (0, 0, 10, 2.5, 1, 28, "No"),  # clinical 4; 10/7: PD not liked (coordinator only)
    "Wayne State": (3.33, 0, 10, None, None, 21, "TBD"),  # clinical 6
}


def teaching(name, clinical, research=None):
    """Teaching/Research composite: 65% clinical + 35% research."""
    research = RESEARCH[name] if research is None else research
    return TEACHING_SPLIT[0] * clinical + TEACHING_SPLIT[1] * research


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
        n: (teaching(n, c), f, g, round(culture(*rest, emr_good=n not in BAD_EMR), 4))
        for n, (c, f, g, *rest) in PROGRAMS.items()
    }


# Bottom five (2026-10-09): Barath re-orders the programs ranked 6-10 by the main formula using
# only Field (Heme/Onc on top) and Geography, 40/60 ("everything else doesn't matter to me").
# Membership comes from the main score; they stay below the top five. Exact ties fall back to
# the main score (Barath's choice; e.g. Wayne State vs Ann Arbor).
# 2026-10-09: added a third bottom-five criterion, MD Anderson regret, at 1/3; Field and
# Geography share the other 2/3 in their 40/60 ratio.
BOTTOM_N = 5
BOTTOM_WEIGHTS = {"field": 0.4 * 2 / 3, "geography": 0.6 * 2 / 3, "regret": 1 / 3}

# How much Barath would regret matching here instead of MD Anderson leukemia (percent).
# Henry Ford "20-30%" -> 25. Scored 0-10 by spreading his values evenly: least regret = 10,
# most regret = 0. Programs without an answer get the neutral 5.
MDA_REGRET_PCT = {
    "UMass Chan": 20,  # 10/10: "same as LSU"
    "LSU New Orleans": 20,  # 10/10; in the top five now, but counts if it crosses the #5/#6 line
    "Henry Ford Providence": 25,
    "NGMC": 40,
    "ETSU": 60,
    "Wayne State": 100,
    "Ann Arbor": 100,
}


def regret_score(name):
    if name not in MDA_REGRET_PCT:
        return NEUTRAL
    lo, hi = min(MDA_REGRET_PCT.values()), max(MDA_REGRET_PCT.values())
    return 10 * (hi - MDA_REGRET_PCT[name]) / (hi - lo)


def bottom_score(name, v):
    w = BOTTOM_WEIGHTS
    return w["field"] * v[1] + w["geography"] * v[2] + w["regret"] * regret_score(name)


def two_tier_order(score, m):
    """Main-formula order for the top, then the bottom five re-ordered by Field, Geography and MDA regret."""
    main = final_order(score, m)
    top, bottom = main[:-BOTTOM_N], main[-BOTTOM_N:]
    bottom = sorted(bottom, key=lambda n: (-round(bottom_score(n, m[n]), 6), -score[n]))
    return top + bottom


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
    for i, n in enumerate(two_tier_order(score, m), 1):
        bs = f" bottom5={bottom_score(n, m[n]):.3f} regret={regret_score(n):.2f}" if i > len(m) - BOTTOM_N else ""
        print(f"{i:>2} (raw {r[n]}) {n:<22} {score[n]:.3f}{bs}  T={m[n][0]:<5.3f} F={m[n][1]:<5} G={m[n][2]:<3} C={m[n][3]:<5} TOPSIS#{tr[n]} C*={t[n][2]:.4f}")
    # sensitivity: +/-10% per weight
    analysis.WEIGHTS = WEIGHTS
    moves = {n: set([r[n]]) for n in m}
    for i in range(4):
        for f in (0.9, 1.1):
            s = analysis.weighted_sum(analysis.perturb(i, f))
            for n, k in ranks(s).items():
                moves[n].add(k)
    print("rank range under +/-10%:", {n: (min(v), max(v)) for n, v in moves.items()})
