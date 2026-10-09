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

Whenever showing the rank list, show ONE table with the full per-category breakdown by default (standing rule, Barath 2026-10-09: "show me the table with scores in each category"). He should never have to ask for "the breakdown."

Columns, in order: Rank | Program | Specialty | Teaching/Research (53.2%) | Field (23.7%) | Geography (13.6%) | Culture (9.5%) | Interview read | 24-hr call | Moonlighting | **Total**.
- Each of the four weighted criteria shows **raw score → weighted points** (e.g. `8 → 4.26`), so the points visibly add up to the Total.
- The three Culture sub-parts show their raw inputs: interview read 0–10 (mark neutral unknowns "5 (N)"), call "Fav 10" / "Unfav 0" / "N", moonlighting Yes / No / TBD.
- Total is the composite score to 3 decimals, in bold.
- Add a rank-change arrow (↑/↓) next to the rank when it moved since the last shown table.

Never split it into separate per-criterion tables, and never show rank alone. Mark any rank decided by the tiebreak rule rather than the score. If the weights or criteria change, update the headers and percentages but keep everything in one table. Compute the cells with the script (rebuild.py) rather than by hand. The Legend page leaderboard may keep the shorter raw-score table.

## Current formula (rebuilt from scratch 2026-09-29, verify against the latest section of the Notion Legend page since this changes)

Claude based Rank = 0.532 x Teaching/Research + 0.237 x Field Preference + 0.136 x Geography + 0.095 x Culture.

The weights were derived with AHP from Barath's own pairwise judgments (2026-09-29): Teaching a bit more than Field (2x), Teaching much more than Geography and than Culture (5x each), Field a bit more than Geography and than Culture (2x each), Geography a bit more than Culture (2x). Consistency ratio 0.025 (acceptable, under 0.10). He explicitly confirmed these supersede his 2026-09-25 "geography first" statement. If he revises any pairwise judgment, recompute the eigenvector weights and CR rather than hand-editing percentages.

All criteria are on a 0 to 10 scale.

- **Teaching/Research**: the fellowship's own faculty strength (PhD bench, research leadership, trials, faculty size). Barath assigns this per program; never leave a TBD stored as 0, since at 53% weight a placeholder 0 dominates the result. Ask him instead.
- **Field Preference**: future salary and job-finding potential given his visa status. Four tiers, spaced evenly (revised 2026-10-07; Barath: "make MCW, NGMC, ETSU the same field preference score"): Heme/Onc 10 > Critical Care, including pure CCM, PCCM and ID/CCM Combined, 6.67 > ID with an optional Critical Care year 3.33 (Tufts only) > plain ID 0. Heme/Onc is strictly above Critical Care, not tied. If Barath moves a specialty between tiers, re-space all tiers evenly.
- **Geography**: Barath's stated location order spaced evenly across 0 to 10 (revised 2026-10-04: "MCW Wisconsin, the geography is the same as NGMC"). Five tiers: Michigan (Henry Ford, Ann Arbor, Wayne State) 10 > Boston area (Tufts, UMass Chan) 7.5 > Milwaukee/MCW = Gainesville/NGMC 5 > New Orleans/LSU 2.5 > Augusta/MCG and Johnson City/ETSU 0. Metro status (Indian community, nightlife, transit, international airport) is already reflected in this order. If Barath moves a city between tiers, re-space all tiers evenly rather than just editing one value.
- **Culture**: a composite, because Barath counts call and moonlighting as part of a program's culture. Culture = 0.625 x interview read + 0.25 x 24-hour call + 0.125 x moonlighting. On 2026-10-06 Barath removed leave and EMR ("Can we remove this leave policy from this equation? And the EMR."); the remaining three were rescaled in proportion from 45/18/9. Vacation days and EMR stay in Notion as reference data only and are never scored.
  - Interview read: 2.5 points each for liking the PD, 2+ faculty, the fellows, the coordinator. An item he feels neutral about ("didn't like, didn't dislike") or could only partly judge (met just one faculty member, whom he liked) gets half credit, 1.25, the same as any other unknown. An item that can't exist (no fellows yet at a new program, e.g. NGMC's first cohort) is also neutral 1.25, not 0 (Barath, 2026-10-06).
  - 24-hour call: favorable 10 only if fellows take no call at all; unfavorable 0 if any call exists, home/pager call included (Barath, 2026-10-02: "the fact that the call exists itself is unfavorable"). A separate night-float system where fellows take no call counts as favorable (MCW, confirmed 2026-10-02; Ann Arbor has no call after 7 PM). Exception (2026-10-06): light call of no more than one day a week, which Barath called "bearable", counts as favorable (Tufts).
  - Moonlighting: Yes 10, No 0.
  - Anything unknown or not yet assessed, including the interview read before the interview happens, is a neutral 5. Never carry a pre-interview guess as a real score.

## Verify every input with Barath, program by program

Barath's explicit instruction (2026-09-29): do not rely on Notion values alone. Notion data has drifted and held placeholders before. When rescoring or rebuilding, walk through each program individually, one program per round, and confirm its Teaching/Research, interview read (as a pick-which-you-liked list of PD, faculty, fellows, coordinator), 24-hour call and moonlighting with him, showing the current Notion value as the default. Field and Geography follow the fixed rules above, so state them for confirmation rather than asking open-ended. Show him the resulting table for approval before writing anything to Notion.

## Confirmed inputs snapshot (updated 2026-10-07)

A dated reference copy only. The live values are in Notion and win on any difference. Neutral = not yet known, counts as 5. Pending values are tracked in the "Still to be decided" checklist of the latest Legend section (mirrored in fellowship-rank-analysis/TBD.md on GitHub); show that checklist when Barath asks what's still undecided.

Vacation days and EMR (only Wayne State/DMC is bad, Cerner/Oracle Health) are kept as reference and are not scored.

| Rank | Program | Teaching | Field | Geography | Interview read | 24-hr call | Moonlighting | Culture | Score |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Tufts | 10 | 3.33 (optional CCM year confirmed by Barath 10/6; ~6% of grads) | 7.5 | 10 (all four, 10/6) | Favorable (no more than 1 day/week, "bearable") | No (contract: visa holders can't moonlight) | 8.75 | 7.960 |
| 2 | LSU New Orleans | 8 | 10 | 2.5 | 5 (faculty, fellows; PD and coordinator not liked) | Unfavorable (home call: weeknight + weekend, per 2026 manual) | No (manual: J-1 may not moonlight; 10/9) | 3.125 | 7.263 |
| 3 | MCW | 8 | 6.67 | 5 | 7.5 (faculty, fellows, coordinator; PD not liked 10/7) | Favorable (separate night float) | No | 7.1875 | 7.200 |
| 4 | MCG | 8 | 10 | 0 | 6.25 (fellows, coordinator, faculty half credit; PD not liked 10/7) | Unfavorable | Yes | 5.15625 | 7.116 |
| 5 | Henry Ford Providence | 4 | 10 | 10 | 2.5 (fellows only; revised 10/6) | Unfavorable (home call) | No | 1.5625 | 6.006 |
| 6 | UMass Chan | 8 | 0 | 7.5 | Neutral (interview 10/16) | Neutral | TBD | 5.0 | 5.751 |
| 7 | ETSU | 6 | 6.67 | 0 | 7.5 (PD, faculty, fellows; interview done 9/18) | Neutral (ask at fellows' meet-and-greet) | TBD | 6.5625 | 5.396 |
| 8 | Wayne State | 6 ("has all the resources") | 0 | 10 | Neutral (interview 10/27) | Neutral | TBD | 5.0 | 5.027 |
| 9 | NGMC | 4 | 6.67 | 5 | 8.75 (PD, faculty, coordinator; fellows neutral 1.25 since no fellows exist, first cohort, 10/6) | Unfavorable | No | 5.46875 | 4.908 |
| 10 | Ann Arbor | 4 | 0 | 10 | 2.5 (coordinator only; PD not liked 10/7) | Favorable (no call after 7 PM) | No | 4.0625 | 3.874 |

Wayne State research note (checked 2026-09-29 on ClinicalTrials.gov): DMC Harper University Hospital is an actively recruiting site on the Phase 3 fosmanogepix vs caspofungin/fluconazole candidemia trial (NCT05421858), and Wayne State has sponsored ID trials before (e.g. a Phase 4 ceftaroline skin-infection trial, NCT02582203, completed 2016). No Wayne State-sponsored ID trial is currently recruiting.

## After each interview: pull the recording (added 2026-10-02)

If Barath recorded the interview, find it in Plaud (list_files filtered by the interview date) and read the ENTIRE transcript, not a summary; say how much was read. Add an "Interview Debrief" section at the top of the program's Interview Tracker page with: source and caveats (speaker labels are unreliable and side chatter gets garbled, so mark unclear parts "(unclear)"); scoring inputs with evidence quotes; corrections to earlier research on the page; rotation structure; education; research; jobs/outcomes; benefits; Barath's interview questions and answers (useful for later interviews); and an open-questions checklist. Henry Ford's page (10/1/2026) is the reference example. Don't raise visa sponsorship as a question or differentiator: every program Barath interviewed with sponsors J-1 (confirmed 2026-10-02). If the recording contradicts a score Barath gave (e.g. he scored call unfavorable but the recording describes home call only), flag it and ask; never override his call silently.

## When Barath gives a tier hierarchy without exact numbers

Barath often states relative order only and expects Claude to assign the actual point values. Default to even linear spacing across the criterion's established range, preserving his stated tier order and tie groupings exactly. If he says something like "you do it, best statistical way," even spacing across the full range is the right call, do not ask, just do it and show the resulting numbers.

If a rearrange or rescale is ambiguous in a way that would meaningfully change relative order or ripple unpredictably (not just relabel the same order with different numbers), ask with a short set of concrete options rather than guessing.

## Ties and robustness

Barath's tiebreak rule (2026-09-29, clarified 2026-10-02): the tiebreak applies only when two composite scores are actually tied (equal at the 3 decimals shown), never to near-ties; a higher score always wins, however small the gap. Break a real tie by Geography first, then Field Preference, then familiarity (NGMC is his home program, so it wins a tie that gets that far). Always say in the reply when a tiebreak, not the score, decided an order, e.g. "LSU #2 over X on the Geography tiebreak (both 7.527)." If the chain still can't separate them, flag the tie explicitly rather than inventing an order.

## Robustness report: part of every rescore (Barath, 2026-10-06)

After **every** scoring change (a new interview input, a rule change or a weight change), run `python3 robustness.py` in fellowship-rank-analysis/ (barathprashanth18196/newbierepository) before reporting. It runs eight checks:
1. ±10% and ±20% one-at-a-time weight sensitivity.
2. Weight stability: the smallest single-weight change that flips each adjacent pair. Under 10% is FRAGILE; over 50% is solid.
3. Teaching break-even: the Teaching points each program needs to pass the one above.
4. Pending inputs: best and worst-case rank for every program with unknowns.
5. Leave-one-criterion-out.
6. Alternative methods: equal weights, rank-order centroid, weighted product, TOPSIS.
7. Monte Carlo, scenarios A and B (montecarlo.py).
8. Gut check: Spearman correlation between the model rank and Barath's own "My Rank" column in Notion. Refresh MY_RANK in robustness.py from Notion first.

Report it in the reply **and** in the new Legend section as a short "Robustness" block, directly under the one-table leaderboard:
- Which adjacent pairs are FRAGILE, and what would flip them.
- The Monte Carlo P(#1) and P(top 3) for the top programs.
- Any pending input that could move a program, with its best and worst rank.
- Any program whose model rank and gut rank differ by 3 or more, flagged for discussion. Never silently resolve these.

Keep it to a few bullets. The full output stays in the script, not in Notion.

**Status (2026-10-06):** Barath says My Rank is out of date, so check 8 is switched off (MY_RANK_CURRENT = False) until he gives a fresh gut order.

## Final check before certifying the rank list (agreed 2026-10-06)

After the last interview (Wayne State, 10/27) and before the Nov 18 deadline, run these in order:
1. **Fresh gut order first:** Barath writes his gut ranking 1 to 10 **before** seeing any model scores, so the model can't anchor him. Save it to the My Rank column and set MY_RANK_CURRENT = True.
2. **Blind re-scoring:** ask for Teaching/Research (and the interview read items) for all 10 programs **without** showing the old values. If any score moves by more than 1 from the stored value, discuss it, then rerun the model.
3. **Regret test:** for every FRAGILE adjacent pair from robustness.py, plus every program where the model and the fresh gut order differ by 3 or more places, ask "If you matched at A instead of B, which would you regret more?" His answer sets the final order for that pair. Record each answer in the Legend.
4. Rerun robustness.py and write the final list to Notion as a new Legend section.

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
