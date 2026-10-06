---
name: fellowship-rank-list-preferences
description: Use when updating, rescoring, or displaying Barath's Claude based Rank fellowship rank list in the Interview Tracker Notion database.
---

# Fellowship rank list preferences

This covers how Barath wants his hematology-oncology/ID/CCM fellowship interview rank list (the "Claude based Rank" column in the Notion "Interview Tracker" database) maintained and displayed. It does not cover adding a brand new program or verifying interview logistics, that is the fellowship-program-intake skill.

## Standing reminders (added 2026-10-02)

At the start of every rank-list conversation, remind Barath of both:
1. **New weighting for the bottom five:** he said he may give a different weighting for the bottom five programs (as of 2026-10-04: UMass Chan, Wayne State, NGMC, ETSU, Ann Arbor). Ask whether it's ready; never invent one.
2. **Culture still unfilled:** list every program with Culture inputs still counting as a neutral 5, from the "Culture still unfilled" checklist in the latest Legend section. Drop items as he fills them in.

## Display format, always

Whenever showing the rank list, show ONE table: rank, program, specialty, composite score, and every scoring criterion's value, all in the same table. Never split the breakdown into separate per criterion tables and never show rank alone without the breakdown. Current columns: Rank, Program, Specialty, Score, Teaching/Research (53.2%), Field Preference (23.7%), Geography (13.6%), Culture (9.5%). Mark any rank decided by the tiebreak rule rather than the score. When Barath asks for "the breakdown," also show each criterion as raw score -> weighted points, plus Culture's four sub-parts, still in the same single table. If the weights or criteria change, update the column headers and percentages to match, but keep everything in one table.

## Current formula (rebuilt from scratch 2026-09-29, verify against the latest section of the Notion Legend page since this changes)

Claude based Rank = 0.532 x Teaching/Research + 0.237 x Field Preference + 0.136 x Geography + 0.095 x Culture.

The weights were derived with AHP from Barath's own pairwise judgments (2026-09-29): Teaching a bit more than Field (2x), Teaching much more than Geography and than Culture (5x each), Field a bit more than Geography and than Culture (2x each), Geography a bit more than Culture (2x). Consistency ratio 0.025 (acceptable, under 0.10). He explicitly confirmed these supersede his 2026-09-25 "geography first" statement. If he revises any pairwise judgment, recompute the eigenvector weights and CR rather than hand-editing percentages.

All criteria are on a 0 to 10 scale.

- **Teaching/Research**: the fellowship's own faculty strength (PhD bench, research leadership, trials, faculty size). Barath assigns this per program; never leave a TBD stored as 0, since at 53% weight a placeholder 0 dominates the result. Ask him instead.
- **Field Preference**: future salary and job-finding potential given his visa status. Five tiers, spaced evenly: Heme/Onc 10 > Critical Care, pure CCM or PCCM 7.5 > ID/CCM Combined 5 (can work in either field) > ID with an optional Critical Care year 2.5 (Tufts is the only one as of 2026-09-29) > plain ID 0. Heme/Onc is strictly above Critical Care, not tied.
- **Geography**: Barath's stated location order spaced evenly across 0 to 10 (revised 2026-10-04: "MCW Wisconsin, the geography is the same as NGMC"). Five tiers: Michigan (Henry Ford, Ann Arbor, Wayne State) 10 > Boston area (Tufts, UMass Chan) 7.5 > Milwaukee/MCW = Gainesville/NGMC 5 > New Orleans/LSU 2.5 > Augusta/MCG and Johnson City/ETSU 0. Metro status (Indian community, nightlife, transit, international airport) is already reflected in this order. If Barath moves a city between tiers, re-space all tiers evenly rather than just editing one value.
- **Culture**: a composite, because Barath counts call, moonlighting and leave as part of a program's culture. Culture = 0.45 x interview read + 0.18 x 24-hour call + 0.18 x leave + 0.09 x moonlighting + 0.10 x EMR (EMR added 2026-09-29; the original four were scaled by 0.9 to make room).
  - Interview read: 2.5 points each for liking the PD, 2+ faculty, the fellows, the coordinator. An item he feels neutral about ("didn't like, didn't dislike") or could only partly judge (met just one faculty member, whom he liked) gets half credit, 1.25, the same as any other unknown.
  - 24-hour call: favorable 10 only if fellows take no call at all; unfavorable 0 if any call exists, home/pager call included (Barath, 2026-10-02: "the fact that the call exists itself is unfavorable"). A separate night-float system where fellows take no call counts as favorable (MCW, confirmed 2026-10-02; Ann Arbor has no call after 7 PM). Exception (2026-10-06): light call of no more than one day a week, which Barath called "bearable", counts as favorable (Tufts).
  - Leave: 20 or more vacation days 10, fewer 0 (yes/no, his choice, not a sliding scale).
  - Moonlighting: Yes 10, No 0.
  - EMR: good 10, bad 0. Wayne State/DMC (Cerner/Oracle Health) is the only bad one; every other program runs Epic.
  - Anything unknown or not yet assessed, including the interview read before the interview happens, is a neutral 5. Never carry a pre-interview guess as a real score.

## Verify every input with Barath, program by program

Barath's explicit instruction (2026-09-29): do not rely on Notion values alone. Notion data has drifted and held placeholders before. When rescoring or rebuilding, walk through each program individually, one program per round, and confirm its Teaching/Research, interview read (as a pick-which-you-liked list of PD, faculty, fellows, coordinator), 24-hour call and moonlighting with him, showing the current Notion value as the default. Field, Geography and Leave follow the fixed rules above, so state them for confirmation rather than asking open-ended. Show him the resulting table for approval before writing anything to Notion.

## Confirmed inputs snapshot (updated 2026-10-06)

A dated reference copy only. The live values are in Notion and win on any difference. Neutral = not yet known, counts as 5. Pending values are tracked in the "Still to be decided" checklist of the latest Legend section (mirrored in fellowship-rank-analysis/TBD.md on GitHub); show that checklist when Barath asks what's still undecided.

| Rank | Program | Teaching | Field | Geography | Interview read | 24-hr call | Vacation days | Moonlighting | EMR | Score |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Tufts | 10 | 2.5 (optional CCM year confirmed by Barath 10/6; ~6% of grads) | 7.5 | 10 (all four, 10/6) | Favorable (no more than 1 day/week, "bearable") | 20 | No (contract: visa holders can't moonlight) | Good | 7.797 |
| 2 | LSU New Orleans | 8 | 10 | 2.5 | 7.5 (PD, faculty, fellows) | Unfavorable | 28 | TBD | Good | 7.595 |
| 3 | MCW | 8 | 7.5 | 5 | 10 (all four) | Favorable (separate night float) | 15 | No | Good | 7.407 |
| 4 | MCG | 8 | 10 | 0 | 7.5 (fellows, coordinator; PD and faculty half credit) | Unfavorable | 21 | Yes | Good | 7.298 |
| 5 | Henry Ford Providence | 4 | 10 | 10 | 5 (faculty, fellows) | Unfavorable (home call) | 20 | No | Good | 6.338 |
| 6 | UMass Chan | 8 | 0 | 7.5 | Neutral (interview 10/16) | Neutral | 20 | TBD | Good | 5.884 |
| 7 | Wayne State | 6 ("has all the resources") | 0 | 10 | Neutral (interview 10/27) | Neutral | 21 | TBD | Bad | 5.065 |
| 8 | NGMC | 4 | 7.5 | 5 | 7.5 (PD, faculty, coordinator) | Unfavorable | 15 | No | Good | 5.001 |
| 9 | ETSU | 6 | 5 | 0 | 7.5 (PD, faculty, fellows; interview done 9/18) | Neutral (ask at fellows' meet-and-greet) | 15 | TBD | Good | 4.921 |
| 10 | Ann Arbor | 4 | 0 | 10 | 5 (PD, coordinator) | Favorable (no call after 7 PM) | 28 | No | Good | 4.139 |

Wayne State research note (checked 2026-09-29 on ClinicalTrials.gov): DMC Harper University Hospital is an actively recruiting site on the Phase 3 fosmanogepix vs caspofungin/fluconazole candidemia trial (NCT05421858), and Wayne State has sponsored ID trials before (e.g. a Phase 4 ceftaroline skin-infection trial, NCT02582203, completed 2016). No Wayne State-sponsored ID trial is currently recruiting.

## After each interview: pull the recording (added 2026-10-02)

If Barath recorded the interview, find it in Plaud (list_files filtered by the interview date) and read the ENTIRE transcript, not a summary; say how much was read. Add an "Interview Debrief" section at the top of the program's Interview Tracker page with: source and caveats (speaker labels are unreliable and side chatter gets garbled, so mark unclear parts "(unclear)"); scoring inputs with evidence quotes; corrections to earlier research on the page; rotation structure; education; research; jobs/outcomes; benefits; Barath's interview questions and answers (useful for later interviews); and an open-questions checklist. Henry Ford's page (10/1/2026) is the reference example. Don't raise visa sponsorship as a question or differentiator: every program Barath interviewed with sponsors J-1 (confirmed 2026-10-02). If the recording contradicts a score Barath gave (e.g. he scored call unfavorable but the recording describes home call only), flag it and ask; never override his call silently.

## When Barath gives a tier hierarchy without exact numbers

Barath often states relative order only and expects Claude to assign the actual point values. Default to even linear spacing across the criterion's established range, preserving his stated tier order and tie groupings exactly. If he says something like "you do it, best statistical way," even spacing across the full range is the right call, do not ask, just do it and show the resulting numbers.

If a rearrange or rescale is ambiguous in a way that would meaningfully change relative order or ripple unpredictably (not just relabel the same order with different numbers), ask with a short set of concrete options rather than guessing.

## Ties and robustness

Barath's tiebreak rule (2026-09-29, clarified 2026-10-02): the tiebreak applies only when two composite scores are actually tied (equal at the 3 decimals shown), never to near-ties; a higher score always wins, however small the gap. Break a real tie by Geography first, then Field Preference, then familiarity (NGMC is his home program, so it wins a tie that gets that far). Always say in the reply when a tiebreak, not the score, decided an order, e.g. "LSU #2 over X on the Geography tiebreak (both 7.527)." If the chain still can't separate them, flag the tie explicitly rather than inventing an order.

After any formula change, rerun TOPSIS and a +/-10% weight sensitivity check (script: fellowship-rank-analysis/rebuild.py in barathprashanth18196/newbierepository) and mention any rank that isn't stable. For a fuller picture, run montecarlo.py in the same folder: it varies the weights and every unknown input 20,000 times and reports each program's chance of finishing #1, top 3 and top 5. As of 2026-09-29, MCW is #1 in about 48% of runs; Henry Ford, LSU, Tufts and MCG form a top-5 cluster whose internal order is not settled until their interviews happen.

## Notion is the single source of truth (Barath's decision, 2026-09-29)

Every Claude session can read and write Notion, so Notion is the official record. Before doing any math, read the current state from Notion, not from this skill's snapshot or any other copy:

- **Live values:** the Interview Tracker data source (collection://0c47349b-53fa-4599-9325-80a711395c44). The Culture column stores the composite Culture score.
- **Rules, history and pending values:** the "Rank List Scoring Legend" page (https://app.notion.com/p/3d650330e23b814cbd7dd74457fd5872). Its highest-numbered section is the current formula and leaderboard; section 21 (2026-09-29) is the from-scratch rebuild. The "Still to be decided" checklist in the latest section is the official list of pending values.

If Notion disagrees with this skill's snapshot, Notion wins; mention the difference to Barath.

## Every change, sync in this order

1. **Notion Interview Tracker (required):** update the live properties on every affected program's page, then re-query the data source fresh and confirm the written values match what you intended, before telling Barath it is done. Never report a Notion write as successful without this re-verification.
2. **Notion Legend page (required):** append a new numbered section (never renumber or delete old ones) describing what changed, why, the exact new values, and the recomputed leaderboard in the one-table format. Carry the "Still to be decided" checklist forward into the new section, ticking off anything resolved.
3. **GitHub (when working from Claude Code):** update rebuild.py and TBD.md in barathprashanth18196/newbierepository/fellowship-rank-analysis, rerun the scripts, commit and push.
4. **Cowork project doc and memory file (optional mirrors):** claude/rank-list-scoring-status.md and the memory file are no longer the record. Update them only when the session can reach them (a Cowork chat in that project). Never block on them or ask Barath to paste into them; a Cowork session can catch up by reading the latest Legend section.

Do steps 1 and 2 for every scoring change, even a small one. Barath relies on Notion staying current across sessions.

**Only a rule change needs a skill update.** Score changes live in Notion and need no skill upload. If you change a rule (formula, weights, scales, tiebreak, sync process), update this file and remind Barath he has to re-upload the skill in claude.ai Settings, since sessions can't install skills themselves.

## Verification habit

Notion data has drifted unintentionally more than once in this project (values reverting, rank numbers colliding, whole properties disappearing). Before confirming any "apply to Notion" request is done, re-query the live data source and compare against your intended state, not just trust that your write calls succeeded. Fix and note any drift you find rather than reporting stale numbers as current.
