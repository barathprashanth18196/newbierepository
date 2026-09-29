---
name: fellowship-rank-list-preferences
description: Use when updating, rescoring, or displaying Barath's Claude based Rank fellowship rank list in the Interview Tracker Notion database.
---

# Fellowship rank list preferences

This covers how Barath wants his hematology-oncology/ID/CCM fellowship interview rank list (the "Claude based Rank" column in the Notion "Interview Tracker" database) maintained and displayed. It does not cover adding a brand new program or verifying interview logistics, that is the fellowship-program-intake skill.

## Display format, always

Whenever showing the rank list, show ONE table: rank, program, specialty, composite score, and every scoring criterion's value, all in the same table. Never split the breakdown into separate per criterion tables and never show rank alone without the breakdown. Current columns: Rank, Program, Specialty, Score, Teaching/Research (53.2%), Field Preference (23.7%), Geography (13.6%), Culture (9.5%). Mark any rank decided by the tiebreak rule rather than the score. When Barath asks for "the breakdown," also show each criterion as raw score -> weighted points, plus Culture's four sub-parts, still in the same single table. If the weights or criteria change, update the column headers and percentages to match, but keep everything in one table.

## Current formula (rebuilt from scratch 2026-09-29, verify against the live project doc since this changes)

Claude based Rank = 0.532 x Teaching/Research + 0.237 x Field Preference + 0.136 x Geography + 0.095 x Culture.

The weights were derived with AHP from Barath's own pairwise judgments (2026-09-29): Teaching a bit more than Field (2x), Teaching much more than Geography and than Culture (5x each), Field a bit more than Geography and than Culture (2x each), Geography a bit more than Culture (2x). Consistency ratio 0.025 (acceptable, under 0.10). He explicitly confirmed these supersede his 2026-09-25 "geography first" statement. If he revises any pairwise judgment, recompute the eigenvector weights and CR rather than hand-editing percentages.

All criteria are on a 0 to 10 scale.

- **Teaching/Research**: the fellowship's own faculty strength (PhD bench, research leadership, trials, faculty size). Barath assigns this per program; never leave a TBD stored as 0, since at 53% weight a placeholder 0 dominates the result. Ask him instead.
- **Field Preference**: future salary and job-finding potential given his visa status. Five tiers, spaced evenly: Heme/Onc 10 > Critical Care, pure CCM or PCCM 7.5 > ID/CCM Combined 5 (can work in either field) > ID with an optional Critical Care year 2.5 (Tufts is the only one as of 2026-09-29) > plain ID 0. Heme/Onc is strictly above Critical Care, not tied.
- **Geography**: Barath's stated location order spaced evenly across 0 to 10: Michigan (Henry Ford, Ann Arbor, Wayne State) 10 > Milwaukee/MCW (close to Michigan) 8 > Boston area (Tufts, UMass Chan) 6 > Gainesville/NGMC 4 > New Orleans/LSU 2 > Augusta/MCG and Johnson City/ETSU 0. Metro status (Indian community, nightlife, transit, international airport) is already reflected in this order.
- **Culture**: a composite, because Barath counts call, moonlighting and leave as part of a program's culture. Culture = 0.45 x interview read + 0.18 x 24-hour call + 0.18 x leave + 0.09 x moonlighting + 0.10 x EMR (EMR added 2026-09-29; the original four were scaled by 0.9 to make room).
  - Interview read: 2.5 points each for liking the PD, 2+ faculty, the fellows, the coordinator. An item he feels neutral about ("didn't like, didn't dislike") or could only partly judge (met just one faculty member, whom he liked) gets half credit, 1.25, the same as any other unknown.
  - 24-hour call: favorable (no true 24-hour in-house call) 10, unfavorable 0.
  - Leave: 20 or more vacation days 10, fewer 0 (yes/no, his choice, not a sliding scale).
  - Moonlighting: Yes 10, No 0.
  - EMR: good 10, bad 0. Wayne State/DMC (Cerner/Oracle Health) is the only bad one; every other program runs Epic.
  - Anything unknown or not yet assessed, including the interview read before the interview happens, is a neutral 5. Never carry a pre-interview guess as a real score.

## Verify every input with Barath, program by program

Barath's explicit instruction (2026-09-29): do not rely on Notion values alone. Notion data has drifted and held placeholders before. When rescoring or rebuilding, walk through each program individually, one program per round, and confirm its Teaching/Research, interview read (as a pick-which-you-liked list of PD, faculty, fellows, coordinator), 24-hour call and moonlighting with him, showing the current Notion value as the default. Field, Geography and Leave follow the fixed rules above, so state them for confirmation rather than asking open-ended. Show him the resulting table for approval before writing anything to Notion.

## Confirmed inputs snapshot (2026-09-29, verified with Barath one program at a time)

Starting point for the next rescoring, not a substitute for re-verifying. Neutral = not yet known, counts as 5. Everything still pending is tracked in fellowship-rank-analysis/TBD.md in barathprashanth18196/newbierepository; keep that file current and show it when Barath asks what's still undecided.

| Rank | Program | Teaching | Field | Geography | Interview read | 24-hr call | Vacation days | Moonlighting | EMR | Score |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MCW | 8 | 7.5 | 8 | 10 (all four) | Favorable | 15 | No | Good | 7.815 |
| 2 | Henry Ford Providence | 6 | 10 | 10 | Neutral (interview 10/1) | Neutral | 20 | TBD | Good | 7.530 |
| 3 | LSU New Orleans | 8 | 10 | 2 | 7.5 (PD, faculty, fellows) | Unfavorable | 28 | TBD | Good | 7.527 |
| 4 | Tufts | 10 | 2.5 | 6 | Neutral (interview 10/6) | Neutral | 20 | TBD | Good | 7.337 |
| 5 | MCG | 8 | 10 | 0 | 7.5 (fellows, coordinator; PD and faculty half credit) | Unfavorable | 21 | Yes | Good | 7.298 |
| 6 | UMass Chan | 8 | 0 | 6 | Neutral (interview 10/16) | Neutral | 20 | TBD | Good | 5.680 |
| 7 | Wayne State | 6 ("has all the resources") | 0 | 10 | Neutral (interview 10/27) | Neutral | 21 | TBD | Bad | 5.065 |
| 8 | NGMC | 4 | 7.5 | 4 | 7.5 (PD, faculty, coordinator) | Unfavorable | 15 | No | Good | 4.865 |
| 9 | ETSU | 6 | 5 | 0 | 7.5 (PD, faculty, fellows) | Neutral (ICU months only, 24-hr vs night float being checked with fellows) | 15 | TBD | Good | 4.921 |
| 10 | Ann Arbor | 4 | 0 | 10 | 5 (PD, coordinator) | Favorable | 28 | No | Good | 4.139 |

Wayne State research note (checked 2026-09-29 on ClinicalTrials.gov): DMC Harper University Hospital is an actively recruiting site on the Phase 3 fosmanogepix vs caspofungin/fluconazole candidemia trial (NCT05421858), and Wayne State has sponsored ID trials before (e.g. a Phase 4 ceftaroline skin-infection trial, NCT02582203, completed 2016). No Wayne State-sponsored ID trial is currently recruiting.

## When Barath gives a tier hierarchy without exact numbers

Barath often states relative order only and expects Claude to assign the actual point values. Default to even linear spacing across the criterion's established range, preserving his stated tier order and tie groupings exactly. If he says something like "you do it, best statistical way," even spacing across the full range is the right call, do not ask, just do it and show the resulting numbers.

If a rearrange or rescale is ambiguous in a way that would meaningfully change relative order or ripple unpredictably (not just relabel the same order with different numbers), ask with a short set of concrete options rather than guessing.

## Ties and robustness

Barath's tiebreak rule (2026-09-29): two programs whose composite scores are within 0.1 points of each other are a tie. Break it by Geography first, then Field Preference, then familiarity (NGMC is his home program, so it wins a tie that gets that far). Always say in the reply when a tiebreak, not the score, decided an order, e.g. "Henry Ford #2 over LSU on the Geography tiebreak (7.530 vs 7.527)." If the chain still can't separate them, flag the tie explicitly rather than inventing an order.

After any formula change, rerun TOPSIS and a +/-10% weight sensitivity check (script: fellowship-rank-analysis/rebuild.py in barathprashanth18196/newbierepository) and mention any rank that isn't stable.

## Every change, sync to all three places

1. Notion: update the live properties on every affected program's Interview Tracker page, then re-query the data source fresh and confirm the written values match what you intended, before telling Barath it is done. Never report a Notion write as successful without this re-verification.
2. Project doc claude/rank-list-scoring-status.md: append a new numbered chronological entry (do not renumber or delete old entries) describing what changed, why, the exact new values, and the recomputed leaderboard. Update the "Current leaderboard" table and the scoring rubric section if the formula or scale changed.
3. Memory file at the project's rank-list-scoring-status.md path: append a compact summary of the same change, pointing back to the project doc for full detail.

Do all three for every scoring change, even a small one. Barath relies on these staying in sync across sessions.

## Verification habit

Notion data has drifted unintentionally more than once in this project (values reverting, rank numbers colliding, whole properties disappearing). Before confirming any "apply to Notion" request is done, re-query the live data source and compare against your intended state, not just trust that your write calls succeeded. Fix and note any drift you find rather than reporting stale numbers as current.
