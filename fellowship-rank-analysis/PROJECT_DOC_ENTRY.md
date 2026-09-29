# Paste-ready entries (2026-09-29)

This cloud session can't reach the Cowork project files, so these two entries are ready to paste.

## For claude/rank-list-scoring-status.md (append as the next numbered entry)

**Claude-based Rank rebuilt from scratch (2026-09-29).** Barath asked to redo the whole scoring and ranking, verifying every input with him one program at a time. MD Anderson stays excluded. My Rank and Score Rank untouched.

- Formula: 0.532 × Teaching/Research + 0.237 × Field + 0.136 × Geography + 0.095 × Culture. Weights from AHP on Barath's pairwise judgments (Teaching > Field 2×, Teaching > Geography 5×, Teaching > Culture 5×, Field > Geography 2×, Field > Culture 2×, Geography > Culture 2×). CR 0.025.
- Field: Heme/Onc 10, CCM/PCCM 7.5, ID/CCM combined 5, ID + optional CCM 2.5 (Tufts), plain ID 0.
- Geography: Michigan 10, Milwaukee 8, Boston area 6, Gainesville 4, New Orleans 2, Augusta/Johnson City 0.
- Culture (composite, stored in the Culture column): 45% interview read + 18% 24-hr call + 18% leave (≥20 days) + 9% moonlighting + 10% EMR (only Wayne State bad). Unknown = neutral 5.
- Tiebreak: within 0.1 points → Geography, then Field, then home-program familiarity (NGMC).

Current leaderboard (Claude-based Rank):

| Rank | Program | Score | Teaching | Field | Geography | Culture |
|---|---|---|---|---|---|---|
| 1 | MCW | 7.815 | 8 | 7.5 | 8 | 7.3 |
| 2 | Henry Ford Providence (tiebreak over LSU) | 7.530 | 6 | 10 | 10 | 6.4 |
| 3 | LSU New Orleans | 7.527 | 8 | 10 | 2 | 6.625 |
| 4 | Tufts | 7.337 | 10 | 2.5 | 6 | 6.4 |
| 5 | MCG | 7.298 | 8 | 10 | 0 | 7.075 |
| 6 | UMass Chan | 5.680 | 8 | 0 | 6 | 6.4 |
| 7 | Wayne State | 5.065 | 6 | 0 | 10 | 5.4 |
| 8 | NGMC (tiebreak over ETSU) | 4.865 | 4 | 7.5 | 4 | 4.375 |
| 9 | ETSU | 4.921 | 6 | 5 | 0 | 5.725 |
| 10 | Ann Arbor | 4.139 | 4 | 0 | 10 | 6.85 |

Value changes found while verifying: Ann Arbor Teaching 0 (was a TBD placeholder) → 4; Wayne State Teaching → 6; ETSU moonlighting No → TBD; Ann Arbor call favorable, moonlighting No; NGMC call unfavorable. Notion written and re-verified 2026-09-29. Full detail: Legend page section 21; scripts in GitHub barathprashanth18196/newbierepository/fellowship-rank-analysis.

## For the memory file (rank-list-scoring-status.md)

2026-09-29: Claude-based Rank rebuilt from scratch with AHP weights (T 53.2 / F 23.7 / G 13.6 / C 9.5), composite Culture (incl. call, leave, moonlighting, EMR), and a Geography → Field → familiarity tiebreak for scores within 0.1. New order: MCW, Henry Ford, LSU, Tufts, MCG, UMass, Wayne State, NGMC, ETSU, Ann Arbor. Pending inputs tracked in fellowship-rank-analysis/TBD.md and Legend section 21. See project doc for detail.
