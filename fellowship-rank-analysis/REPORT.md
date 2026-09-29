# TOPSIS + Sensitivity Analysis: Fellowship Rank List (2026 Cycle)

Run 2026-09-29 on the 10 active ERAS programs (MD Anderson excluded). Reproducible with `python3 analysis.py` in this folder.

## Summary

**The #1 pick stays the same, but only just.** TOPSIS (a method that ranks each program by how close it sits to a made-up "perfect" program and how far it sits from a made-up "worst" one) gives the same top 5 as your current formula: MCW, then Henry Ford, then LSU, MCG, Tufts. **It breaks the Henry Ford/LSU tie in Henry Ford's favor** (0.7785 vs 0.7705). The reason: Henry Ford's only weak spot is a 6 in Teaching, while LSU has a 2 in Geography, and TOPSIS penalizes one deep hole more than a spread-out shortfall. **Your weights are internally consistent.** The AHP consistency ratio is well under 0.10. **But the top 3 are fragile.** A 10% nudge to one weight is enough to knock MCW off #1 in 3 of 8 scenarios, and the Henry Ford/LSU tie comes down to a single thing: whether Teaching counts exactly twice as much as Geography. #4 through #10 are rock solid. In practice, MCW, Henry Ford and LSU are a statistical three-way tie, and the order among them should come down to your gut, not the third decimal place.

## 1. TOPSIS ranking

**TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) scales each criterion so they're comparable, then scores each program on how close it is to the best possible program (all top scores) and how far it is from the worst possible one (all bottom scores). The closeness score C runs from 0 to 1, and higher is better. Same weights as today (0.35 / 0.30 / 0.175 / 0.175).

| TOPSIS rank | Program | Distance to best | Distance to worst | **C** | Weighted-sum rank (today) | Change |
|---|---|---|---|---|---|---|
| 1 | MCW | 0.0526 | 0.2000 | **0.7919** | 1 | — |
| 2 | Henry Ford Providence | 0.0579 | 0.2037 | **0.7785** | 2 (tie) | tie broken ↑ |
| 3 | LSU New Orleans | 0.0656 | 0.2201 | **0.7705** | 2 (tie) | tie broken ↓ |
| 4 | MCG | 0.0888 | 0.2113 | **0.7040** | 4 | — |
| 5 | Tufts | 0.1535 | 0.1676 | **0.5220** | 5 | — |
| 6 | NGMC (home) | 0.1168 | 0.1250 | **0.5169** | 7 | ↑1 |
| 7 | UMass Chan | 0.1562 | 0.1434 | **0.4785** | 6 | ↓1 |
| 8 | ETSU | 0.1492 | 0.1262 | **0.4581** | 8 | — |
| 9 | Ann Arbor | 0.2085 | 0.1069 | **0.3389** | 9 | — |
| 10 | Wayne State | 0.2016 | 0.0869 | **0.3013** | 10 | — |

What this tells you:
- **The top 5 order is identical** to weighted sum, so the current formula isn't hiding anything big.
- **Henry Ford beats LSU** because it's closest to the ideal program. Its gaps are one moderate miss (Teaching 6). LSU's big miss is Geography 2, and TOPSIS punishes a single deep hole more than weighted sum does. That makes this a principled tiebreak, not a random one.
- **NGMC and UMass Chan swap places.** NGMC is middling everywhere with no zeros, while UMass has a 0 in Field Preference. That's the non-compensatory effect showing up exactly where you'd expect it.
- **MCW's lead is small** (0.7919 vs 0.7785, about 1.3 points on a 100-point scale).

## 2. AHP consistency check on the weights

**AHP** (Analytic Hierarchy Process) derives weights from head-to-head comparisons ("how much more important is Teaching than Geography?"). The **consistency ratio (CR)** measures whether those comparisons contradict each other (e.g. saying A > B, B > C, but C > A). CR under 0.10 is conventionally acceptable.

Two versions of your pairwise matrix were checked:

**(a) Exact ratios implied by your weights** (Teaching:Field 1.17, Teaching:Geo 2, Teaching:Culture 2, Field:Geo 1.71, Field:Culture 1.71, Geo:Culture 1)

| | Teaching | Field | Geography | Culture |
|---|---|---|---|---|
| Teaching | 1 | 1.17 | 2 | 2 |
| Field | 0.86 | 1 | 1.71 | 1.71 |
| Geography | 0.5 | 0.58 | 1 | 1 |
| Culture | 0.5 | 0.58 | 1 | 1 |

λmax = 4.000, **CR = 0.000**. This is perfectly consistent, but that's automatic: any matrix built by dividing one set of weights by itself is consistent by construction. So on its own this doesn't prove much.

**(b) A realistic "by feel" version on AHP's standard 1–9 whole-number scale.** Here Teaching is rated 2× Field, 2× Geography and 2× Culture, Field is 2× Geography and Culture, and Geography equals Culture.

| | Teaching | Field | Geography | Culture |
|---|---|---|---|---|
| Teaching | 1 | 2 | 2 | 2 |
| Field | 1/2 | 1 | 2 | 2 |
| Geography | 1/2 | 1/2 | 1 | 1 |
| Culture | 1/2 | 1/2 | 1 | 1 |

Resulting weights 0.395 / 0.278 / 0.163 / 0.163, λmax = 4.061, **CR = 0.023, well under 0.10.** (If you instead call Teaching and Field "equal," the weights become 0.333 / 0.333 / 0.167 / 0.167 with CR = 0.)

**Bottom line:** your ordinal preferences (Teaching > Field > Geography = Culture) are transitive and coherent, and the weights you picked by feel sit squarely between those two reasonable AHP versions. No red flag and no change recommended. Note that swapping to either AHP version *would* reshuffle the top 3: the Teaching = Field version puts Henry Ford and LSU tied at 8.667 ahead of MCW at 8.557, and the Teaching-heavy version gives MCW 8.748, LSU 8.694, Henry Ford 8.420. That sensitivity is the real story (Section 3).

## 3. Weight sensitivity (±10%, one weight at a time)

Each weight was multiplied by 0.9 or 1.1, and the other three were rescaled proportionally so everything still sums to 1.0. Weighted sum was then recomputed.

### Top 3 in each scenario

| Scenario | Weights (T / F / G / C) | #1 | #2 | #3 | HF − LSU | MCW lead over next |
|---|---|---|---|---|---|---|
| **Baseline** | .350 / .300 / .175 / .175 | MCW 8.651 | HF 8.600 = LSU 8.600 | | 0.000 | +0.051 |
| Teaching −10% | .315 / .316 / .184 / .184 | **HF** 8.740 | MCW 8.578 | LSU 8.525 | +0.215 | **−0.162** |
| Teaching +10% | .385 / .284 / .166 / .166 | MCW 8.724 | **LSU** 8.675 | HF 8.460 | −0.215 | +0.048 |
| Field −10% | .365 / .270 / .183 / .183 | MCW 8.736 | HF 8.540 = LSU 8.540 | | 0.000 | +0.196 |
| Field +10% | .335 / .330 / .168 / .168 | **HF 8.660 = LSU 8.660** | | MCW 8.566 | 0.000 | **−0.094** |
| Geography −10% | .357 / .306 / .158 / .179 | **LSU** 8.740 | MCW 8.665 | HF 8.570 | −0.170 | **−0.075** |
| Geography +10% | .343 / .294 / .193 / .171 | MCW 8.637 | **HF** 8.630 | LSU 8.460 | +0.170 | +0.008 |
| Culture −10% | .357 / .306 / .179 / .158 | MCW 8.622 | HF 8.570 = LSU 8.570 | | 0.000 | +0.052 |
| Culture +10% | .343 / .294 / .171 / .193 | MCW 8.680 | HF 8.630 = LSU 8.630 | | 0.000 | +0.050 |

### Stability by program (rank across baseline + 8 scenarios)

| Program | Baseline rank | Best | Worst | Verdict |
|---|---|---|---|---|
| MCW | 1 | 1 | 3 | **Fragile.** Loses #1 in 3 of 8 scenarios |
| Henry Ford Providence | 2 (tie) | 1 | 3 | **Fragile** |
| LSU New Orleans | 2 (tie) | 1 | 3 | **Fragile** |
| MCG | 4 | 4 | 4 | Robust |
| Tufts | 5 | 5 | 5 | Robust |
| UMass Chan | 6 | 6 | 6 | Robust |
| NGMC | 7 | 7 | 7 | Robust |
| ETSU | 8 | 8 | 9 | Mostly robust (swaps with Ann Arbor only at Teaching −10%) |
| Ann Arbor | 9 | 8 | 9 | Mostly robust |
| Wayne State | 10 | 10 | 10 | Robust |

### Key findings
- **MCW loses #1** when Teaching drops 10% (Henry Ford takes it), when Field rises 10% (Henry Ford and LSU tie for #1), and when Geography drops 10% (LSU takes it). Its baseline lead is only 0.051 points.
- **Henry Ford vs LSU separates only when the Teaching or Geography weight moves.** The two programs score the same on Field (10) and Culture (10). They differ only in Teaching (LSU +4) and Geography (Henry Ford +8). With Teaching at exactly 2× Geography (0.35 vs 0.175), those differences cancel perfectly: 0.35 × 4 = 0.175 × 8 = 1.4. So the tie is an artifact of that 2:1 ratio:
  - Teaching counts **more** than 2× Geography → **LSU** wins
  - Teaching counts **less** than 2× Geography → **Henry Ford** wins
  - Changing the Field or Culture weight can never break this tie.
- **Everything from #4 down is locked in.** No realistic weight tweak moves MCG, Tufts, UMass, NGMC or Wayne State.

## What this means for the decision
1. Your formula isn't broken. TOPSIS agrees on the top 5, and the weights are internally consistent.
2. MCW, Henry Ford and LSU are effectively tied. The gaps between them are smaller than the uncertainty in weights you set by feel.
3. To settle Henry Ford vs LSU, answer one question honestly: *"Is a stronger teaching/research program worth more or less than twice as much as being close to where I want to live?"* More than twice → LSU. Less → Henry Ford. TOPSIS leans Henry Ford because it's more balanced, with no single big weakness.
4. The live Claude based Rank values in Notion were not changed. That's your call.
