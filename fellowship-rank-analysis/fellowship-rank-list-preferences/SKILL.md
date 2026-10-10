---
name: fellowship-rank-list-preferences
description: Use when updating, rescoring, or displaying Barath's Claude based Rank fellowship rank list in the Interview Tracker Notion database.
---

# Fellowship rank list preferences

This covers how Barath wants his hematology-oncology/ID/CCM fellowship interview rank list (the "Claude based Rank" column in the Notion "Interview Tracker" database) maintained and displayed. It does not cover adding a brand new program or verifying interview logistics, that is the fellowship-program-intake skill.

## Standing reminders (added 2026-10-02)

At the start of every rank-list conversation, remind Barath of both:
1. ~~New weighting for the bottom five~~: resolved 2026-10-09 (Field 40 / Geography 60, see below). No longer a reminder.
2. **Culture still unfilled:** list every program with Culture inputs still counting as a neutral 5, from the "Culture still unfilled" checklist in the latest Legend section. Drop items as he fills them in.

## Display format, always

Whenever showing the rank list, show ONE table with the full per-category breakdown by default (standing rule, Barath 2026-10-09: "show me the table with scores in each category"). He should never have to ask for "the breakdown."

Columns, in order: Rank | Program | Clinical | Research | Teaching (54.4%) | Field (20.1%) | Geography (16.1%) | Culture (9.4%) | Interview read | 24-hr call | Moonlighting | **Total**. (Specialty may be dropped when the table gets too wide.)
- Each of the four weighted criteria shows **raw score → weighted points** (e.g. `8 → 4.26`), so the points visibly add up to the Total.
- Clinical and Research show their raw 0–10 scores (Teaching = 0.65 × Clinical + 0.35 × Research).
- The three Culture sub-parts show their 0–10 inputs: interview read (neutral unknowns "5 (N)"), call 10 / 0 / "5 (N)", moonlighting 10 / 0 / "5 (N)".
- Total is the composite score to 3 decimals, in bold.
- **No arrows or change markers in the table** (Barath, 2026-10-09). Rank shows the number only. Below the table, in text, briefly list which programs changed rank (e.g. "Changed: MCG 3→2, MCW 2→3"). Don't narrate up vs down beyond that.

**Split into two sections** (Barath, 2026-10-09: "bottom five, split it in the table"): a **Top five** table with the full columns above, then a **Bottom five** table with Rank | Program | Field (26.7%) raw → pts | Geography (40%) raw → pts | MDA regret (33.3%) % → score → pts | **Bottom-5 score** | Main score (reference). Also show the #6 program as a "(line)" reference row at the bottom of the top-five table, with its main score and the gap to #5. Note any bottom-five tie and that the main score decided it.

Apart from that top/bottom split, never split it into separate per-criterion tables, and never show rank alone. Mark any rank decided by the tiebreak rule rather than the score. If the weights or criteria change, update the headers and percentages but keep everything in one table. Compute the cells with the script (rebuild.py) rather than by hand. The Legend page leaderboard may keep the shorter raw-score table.

## Current formula (rebuilt from scratch 2026-09-29, revised 2026-10-09; verify against the latest section of the Notion Legend page since this changes)

Claude based Rank = 0.544 x Teaching/Research + 0.201 x Field Preference + 0.161 x Geography + 0.094 x Culture.

The weights were derived with AHP from Barath's own pairwise judgments: Teaching a bit more than Field (2x), Teaching much more than Geography and than Culture (5x each), **Field equal to Geography (1x; changed 2026-10-09 from "Field a bit more" 2x, because Barath wanted "a little bit more geography, a little bit less field" and confirmed "fine with 20 and 16")**, Field a bit more than Culture (2x), Geography a bit more than Culture (2x). Consistency ratio 0.032 (acceptable, under 0.10). Before 10/9 the weights were 53.2/23.7/13.6/9.5 (CR 0.025). He explicitly confirmed these supersede his 2026-09-25 "geography first" statement. If he revises any pairwise judgment, recompute the eigenvector weights and CR rather than hand-editing percentages.

**Every criterion and every sub-criterion runs 0 to 10, with Barath's lowest tier at 0 and his top tier at 10** (Barath, 2026-10-09: "I want everything to start from 0 to 10"). When he gives a tier order, spread the tiers evenly from 0 to 10. If he gives direct numbers that don't span 0–10, spread his distinct levels evenly to 0–10 and confirm with him.

- **Teaching/Research** (split 2026-10-09) = **0.65 x Clinical + 0.35 x Research**, the fellowship's own faculty strength. Never leave a TBD stored as 0; at 54% weight a placeholder 0 dominates. Ask him instead.
  - **Clinical**: Barath's direct clinical-teaching scores (10/8/6/4) spread evenly to 0–10: Tufts 10; MCW, MCG, UMass 6.67; LSU, ETSU, Wayne State 3.33; Henry Ford, NGMC, Ann Arbor 0.
  - **Research**: five even tiers from Barath's order (10/9): Tufts 10 (maximum) > MCG 7.5 (second) > UMass 5 (one below MCG) > MCW, LSU, NGMC, Ann Arbor 2.5 (one above lowest) > Henry Ford, ETSU, Wayne State 0 (lowest).
  - Notion stores Clinical, Research and the Teaching/Research composite in separate columns.
- **Field Preference**: future salary and job-finding potential given his visa status. Four tiers, spaced evenly (revised 2026-10-07; Barath: "make MCW, NGMC, ETSU the same field preference score"): Heme/Onc 10 > Critical Care, including pure CCM, PCCM and ID/CCM Combined, 6.67 > ID with an optional Critical Care year 3.33 (Tufts only) > plain ID 0. Heme/Onc is strictly above Critical Care, not tied. If Barath moves a specialty between tiers, re-space all tiers evenly.
- **Bottom five (2026-10-09)**: the programs ranked #6–10 by the main formula are re-ordered among themselves by **0.267 x Field + 0.40 x Geography + 0.333 x MD Anderson regret** only. Barath first said "I will weigh Heme/Onc and geography as the highest. Everything else doesn't matter to me" (Field 40 / Geography 60), then added MDA regret at one-third, with Field and Geography sharing the other two-thirds in their 40/60 ratio.
  - **MDA regret**: how much he'd regret matching there instead of MD Anderson leukemia, stored as "MDA Regret %" in Notion. Answers: LSU 20 (10/10), Henry Ford "20–30%" (25 used), NGMC 40, ETSU 60, Wayne State 100, Ann Arbor 100. Scored 0–10 by spreading his values evenly (least regret 10, most regret 0). No answer = neutral 5, so ask for the regret % of any program near the #5/#6 line (UMass is still missing).
  - **Membership is recomputed on every run from the main score.** Henry Ford sits on the #5/#6 line (Barath: "Henry Ford may end up moving to the top if any of the programs in the top five score lower"). If a top-five program drops below it, Henry Ford moves up and that program is re-scored in the bottom five.
  - They always stay below the top five. Exact bottom-five ties fall back to the main score (his choice: Wayne State 3.257 over Ann Arbor 2.468, both 4.000). Code: rebuild.two_tier_order.
- **Geography**: Barath's stated location order spaced evenly across 0 to 10 (revised 2026-10-04: "MCW Wisconsin, the geography is the same as NGMC"). Five tiers: Michigan (Henry Ford, Ann Arbor, Wayne State) 10 > Boston area (Tufts, UMass Chan) 7.5 > Milwaukee/MCW = Gainesville/NGMC 5 > New Orleans/LSU 2.5 > Augusta/MCG and Johnson City/ETSU 0. Metro status (Indian community, nightlife, transit, international airport) is already reflected in this order. If Barath moves a city between tiers, re-space all tiers evenly rather than just editing one value.
- **Culture**: a composite, because Barath counts call and moonlighting as part of a program's culture. Culture = 0.625 x interview read + 0.25 x 24-hour call + 0.125 x moonlighting. On 2026-10-06 Barath removed leave and EMR ("Can we remove this leave policy from this equation? And the EMR."); the remaining three were rescaled in proportion from 45/18/9. Vacation days and EMR stay in Notion as reference data only and are never scored.
  - Interview read: 2.5 points each for liking the PD, 2+ faculty, the fellows, the coordinator. An item he feels neutral about ("didn't like, didn't dislike") or could only partly judge (met just one faculty member, whom he liked) gets half credit, 1.25, the same as any other unknown. An item that can't exist (no fellows yet at a new program, e.g. NGMC's first cohort) is also neutral 1.25, not 0 (Barath, 2026-10-06).
  - 24-hour call: favorable 10 only if fellows take no call at all; unfavorable 0 if any call exists, home/pager call included (Barath, 2026-10-02: "the fact that the call exists itself is unfavorable"). A separate night-float system where fellows take no call counts as favorable (MCW, confirmed 2026-10-02; Ann Arbor has no call after 7 PM). Exception (2026-10-06): light call of no more than one day a week, which Barath called "bearable", counts as favorable (Tufts).
  - Moonlighting: Yes 10, No 0.
  - Anything unknown or not yet assessed, including the interview read before the interview happens, is a neutral 5. Never carry a pre-interview guess as a real score.

## Verify every input with Barath, program by program

Barath's explicit instruction (2026-09-29): do not rely on Notion values alone. Notion data has drifted and held placeholders before. When rescoring or rebuilding, walk through each program individually, one program per round, and confirm its Clinical and Research scores, interview read (as a pick-which-you-liked list of PD, faculty, fellows, coordinator), 24-hour call and moonlighting with him, showing the current Notion value as the default. Field and Geography follow the fixed rules above, so state them for confirmation rather than asking open-ended. Show him the resulting table for approval before writing anything to Notion.

## Confirmed inputs snapshot (updated 2026-10-09)

A dated reference copy only. The live values are in Notion and win on any difference. Neutral = not yet known, counts as 5. Pending values are tracked in the "Still to be decided" checklist of the latest Legend section (mirrored in fellowship-rank-analysis/TBD.md on GitHub); show that checklist when Barath asks what's still undecided.

Vacation days and EMR (only Wayne State/DMC is bad, Cerner/Oracle Health) are kept as reference and are not scored.

| Rank | Program | Clinical | Research | Field | Geography | Interview read | 24-hr call | Moonlighting | Culture | Score |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Tufts | 10 | 10 | 3.33 (optional CCM year; Tufts ID PD: ~5% of grads go to ID critical care. The 1-year CCM is a separate application; alumni origins not verified) | 7.5 | 10 (all four, 10/6) | Favorable (≤1 day/week, "bearable") | No (contract: visa holders can't moonlight) | 8.75 | 8.139 |
| 2 | MCG | 6.67 | 7.5 | 10 | 0 | 6.25 (fellows, coordinator, faculty half credit; PD not liked 10/7) | Unfavorable | Yes | 5.15625 | 6.281 |
| 3 | MCW | 6.67 | 2.5 | 6.67 | 5 | 7.5 (faculty, fellows, coordinator; PD not liked 10/7) | Favorable (separate night float) | No | 7.1875 | 5.656 |
| 4 | UMass Chan | 6.67 | 5 | 0 | 7.5 | Neutral (interview 10/16) | Neutral | TBD | 5.0 | 4.988 |
| 5 | LSU New Orleans | 3.33 ("same as ETSU", 10/9) | 2.5 | 10 | 2.5 | 5 (faculty, fellows; PD and coordinator not liked) | Unfavorable (home call M–F 24h + ~2 weekends/month during 6–8 F1 inpatient months; confirmed in 10/9 interview recordings) | No (manual: J-1 may not moonlight; 10/9) | 3.125 | 4.360 |
| 6 | Henry Ford Providence | 0 | 0 | 10 | 10 | 2.5 (fellows only; revised 10/6) | Unfavorable (home call) | No | 1.5625 | 3.767 |
| 7 | NGMC | 0 | 2.5 | 6.67 | 5 | 8.75 (PD, faculty, coordinator; fellows neutral 1.25 since no fellows exist, first cohort, 10/6) | Unfavorable | No | 5.46875 | 3.136 |
| 8 | Wayne State | 3.33 ("has all the resources") | 0 | 0 | 10 | Neutral (interview 10/27) | Neutral | TBD | 5.0 | 3.257 |
| 9 | Ann Arbor | 0 | 2.5 | 0 | 10 | 2.5 (coordinator only; PD not liked 10/7) | Favorable (no call after 7 PM) | No | 4.0625 | 2.468 |
| 10 | ETSU | 3.33 | 0 | 6.67 | 0 | 7.5 (PD, faculty, fellows; interview done 9/18) | Neutral (ask at fellows' meet-and-greet) | TBD | 6.5625 | 3.135 |

Ranks 6–10 come from the bottom-five formula (Field 26.7 / Geography 40 / MDA regret 33.3): Henry Ford 9.792, NGMC 6.279, Wayne State 4.000, Ann Arbor 4.000 (tie; main score decides), ETSU 3.445. The Score column is the main-formula score for reference. LSU (regret 20%) would score 7.0 there if it ever crossed the #5/#6 line.

Wayne State research note (checked 2026-09-29 on ClinicalTrials.gov): DMC Harper University Hospital is an actively recruiting site on the Phase 3 fosmanogepix vs caspofungin/fluconazole candidemia trial (NCT05421858), and Wayne State has sponsored ID trials before (e.g. a Phase 4 ceftaroline skin-infection trial, NCT02582203, completed 2016). No Wayne State-sponsored ID trial is currently recruiting.

## After each interview: pull the recording (added 2026-10-02)

If Barath recorded the interview, find it in Plaud (list_files filtered by the interview date) and read the ENTIRE transcript, not a summary; say how much was read. Add an "Interview Debrief" section at the top of the program's Interview Tracker page with: source and caveats (speaker labels are unreliable and side chatter gets garbled, so mark unclear parts "(unclear)"); scoring inputs with evidence quotes; corrections to earlier research on the page; rotation structure; education; research; jobs/outcomes; benefits; Barath's interview questions and answers (useful for later interviews); and an open-questions checklist. Henry Ford's page (10/1/2026) is the reference example. Don't raise visa sponsorship as a question or differentiator: every program Barath interviewed with sponsors J-1 (confirmed 2026-10-02). If the recording contradicts a score Barath gave (e.g. he scored call unfavorable but the recording describes home call only), flag it and ask; never override his call silently.


**Update the Plaud tracker every time (Barath, 2026-10-10):** after each interview, add every recording from that day to the Notion page "Interview Recordings (Plaud)" (https://app.notion.com/p/3f550330e23b81c7a1b7ea73f297969d, under Interview prep1): date, program (page mention), exact Plaud title, length. Barath shares this page with his girlfriend. Plaud's audio links expire in 24 hours, so never paste them; point to the Plaud app's Share instead. Keep MD Anderson (9/29) on it, even though it's excluded from the ranking.
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

**Always update Notion and this skill, every change** (Barath, 2026-10-09: "always update the Notion and the skill"). Score changes go to Notion and to the inputs snapshot here; rule changes also go to the Legend rules toggle and the rule sections here. If you change a rule (formula, weights, scales, tiebreak, sync process), update this file and remind Barath he has to re-upload the skill in claude.ai Settings, since sessions can't install skills themselves.

## Verification habit

Notion data has drifted unintentionally more than once in this project (values reverting, rank numbers colliding, whole properties disappearing). Before confirming any "apply to Notion" request is done, re-query the live data source and compare against your intended state, not just trust that your write calls succeeded. Fix and note any drift you find rather than reporting stale numbers as current.
