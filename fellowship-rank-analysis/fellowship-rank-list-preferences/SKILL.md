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

## Notion writes need approval (Barath, 2026-10-19)

Before changing anything in Notion (tracker rows, Legend, pages, memory), show Barath the exact change and wait for his yes.

## Language (Barath, 2026-10-19)

Write in American English everywhere: chat, Notion, repo files. No British spellings (hemodynamic, randomized, multicenter, pediatric). Paper titles and journal names stay as published.

## Display format, always

Whenever showing the rank list, show ONE table with the full per-category breakdown by default (standing rule, Barath 2026-10-09: "show me the table with scores in each category"). He should never have to ask for "the breakdown." Reinforced 2026-10-20 ("always show me the entire scoring table"): every reply that changes or mentions scores or ranks shows the ENTIRE table (all programs, every category column), never a shortened rank/score list.

**Elaborate scores, every time (Barath, 2026-10-12: "show me elaborate scores moving forward").** Any reply that shows scores or ranks, including a quick "show me the score" or a what-if, uses the full elaborate layout below: the combined all-10 table plus the separate bottom-five table, raw → points for every weighted criterion, Clinical and Research, all three Culture sub-parts, the bottom-five regret math, the neutral-values count, then the "Changed:" line and the Robustness block. Never shorten it to a rank list or a totals-only table unless he asks for the short version (e.g. a message to forward to his mentor). **Reinforced 2026-10-16 ("Moving forward show me everything"):** every rescore reply shows the specialty, Clinical and Research separately (raw → points), Field, Geography, all three Culture sub-parts (interview read, call, moonlighting) with the Culture total, the main score, the bottom-five score, plus the reference columns (MDA regret %, vacation days, EMR) and any provisional or neutral flags. Don't drop the Culture sub-parts even when only one program changed.

Columns, in order: Rank | Program | Clinical | Research | Teaching (35%) | Field (25%) | Geography (22.9%) | Culture (17.1%) | Interview read | 24-hr call | Moonlighting | **Total**. (Specialty may be dropped when the table gets too wide.)
- Each of the four weighted criteria shows **raw score → weighted points** (e.g. `8 → 4.26`), so the points visibly add up to the Total.
- Clinical and Research show their raw 0–10 scores (Teaching = 0.5 × Clinical + 0.5 × Research).
- The three Culture sub-parts show their 0–10 inputs: interview read (neutral unknowns "5 (N)"), call 10 / 0 / "5 (N)", moonlighting 10 / 0 / "5 (N)".
- Total is the composite score to 3 decimals, in bold.
- **No arrows or change markers in the table** (Barath, 2026-10-09). Rank shows the number only. Below the table, in text, briefly list which programs changed rank (e.g. "Changed: MCG 3→2, MCW 2→3"). Don't narrate up vs down beyond that.

**Layout (Barath, 2026-10-13: "combine it with the top five and show me the whole thing, and then separately show me the bottom five table"):** first ONE **combined table of all 10 programs** with the full columns above plus a **Bottom-5 score** column ("—" for ranks 1–5). Ranks 1–5 are ordered by the main score; ranks 6–10 by the bottom-five score, and the table notes this under it. Then a separate **Bottom five** table: Rank | Program | Field (26.7%) raw → pts | Geography (40%) raw → pts | MDA regret (33.3%) % → score → pts | **Bottom-5 score** | Main score (reference). Note any bottom-five tie and that the main score decided it, and call out the #5/#6 gap (main score) in text. (This replaced the 10/9 split into separate Top-five and Bottom-five tables with a "(line)" row.)

Apart from that layout, never split it into separate per-criterion tables, and never show rank alone. Mark any rank decided by the tiebreak rule rather than the score. If the weights or criteria change, update the headers and percentages but keep everything in one table. Compute the cells with the script (rebuild.py) rather than by hand. The Legend page leaderboard may keep the shorter raw-score table.

## Current formula (rebuilt from scratch 2026-09-29, revised 2026-10-09; verify against the latest section of the Notion Legend page since this changes)

Claude based Rank = 0.35 x Teaching/Research + 0.25 x Field Preference + 0.229 x Geography + 0.171 x Culture.

**2026-10-12 (later): Field capped at 25%** ("field no more than 25; adjust the remaining with culture"). The 3.7 points went to Culture (13.4% → 17.1%).

**2026-10-12: Barath set Teaching directly to 35%** ("teaching give 35%"), after comparing what-ifs at 40% and 35%. Field, Geography and Culture were rescaled in proportion from the AHP weights below. This is a direct override, so the consistency ratio no longer applies; the AHP judgments are kept as the record of how the other three relate.

The weights were derived with AHP from Barath's own pairwise judgments: Teaching a bit more than Field (2x), Teaching much more than Geography and than Culture (5x each), **Field equal to Geography (1x; changed 2026-10-09 from "Field a bit more" 2x, because Barath wanted "a little bit more geography, a little bit less field" and confirmed "fine with 20 and 16")**, Field a bit more than Culture (2x), Geography a bit more than Culture (2x). Consistency ratio 0.032 (acceptable, under 0.10). Before 10/9 the weights were 53.2/23.7/13.6/9.5 (CR 0.025). He explicitly confirmed these supersede his 2026-09-25 "geography first" statement. If he revises any pairwise judgment, recompute the eigenvector weights and CR rather than hand-editing percentages.

**Every criterion and every sub-criterion runs 0 to 10, with Barath's lowest tier at 0 and his top tier at 10** (Barath, 2026-10-09: "I want everything to start from 0 to 10"). When he gives a tier order, spread the tiers evenly from 0 to 10. If he gives direct numbers that don't span 0–10, spread his distinct levels evenly to 0–10 and confirm with him.

- **Teaching/Research** (split 2026-10-09; changed to 50/50 on 2026-10-12, "equal importance to both") = **0.5 x Clinical + 0.5 x Research**, the fellowship's own faculty strength. Never leave a TBD stored as 0; at 35% weight a placeholder 0 still dominates. Ask him instead.
  - **Clinical**: Barath's direct clinical-teaching scores (10/8/6/4) spread evenly to 0–10: Tufts 10; MCW, UMass 6.67; MCG (10/12, "same as LSU"), LSU, ETSU, Wayne State 3.33; Henry Ford, NGMC, Ann Arbor 0.
  - **Research**: even tiers from Barath's order. Since 2026-10-13 ("MCG and UMass research same tier, adjust the whole tier"), 4 tiers: Tufts 10 > MCG = UMass 6.67 > MCW, LSU, NGMC, Ann Arbor 3.33 > Henry Ford, ETSU, Wayne State 0. 2026-10-16 ("Research is 10 for UMass"): Tufts = Ohio State = UMass 10 > MCG 6.67 > MCW, LSU, NGMC, Ann Arbor 3.33 > Henry Ford, ETSU, Wayne State 0 (still 4 tiers, no re-spacing). Later 10/16 ("Ann Arbor research is 0"): Tufts = Ohio State = UMass 10 > MCG 6.67 > MCW, LSU, NGMC 3.33 > Henry Ford, ETSU, Wayne State, Ann Arbor 0. (Before that, 5 tiers: Tufts 10 > MCG 7.5 > UMass 5 > MCW/LSU/NGMC/AA 2.5 > HF/ETSU/WS 0.) 2026-10-19 ("wayne state research is 10"; "mcw and umass same as mcg"): **Tufts = Ohio State = Wayne State 10 > MCG = MCW = UMass 6.67 > LSU = NGMC 3.33 > Henry Ford = ETSU 0** (Ann Arbor 0 but not ranked). Still 4 tiers. 2026-10-20 (after the PubMed and faculty-page checks: "score wayne research 0, mcg research 10"): **Tufts = Ohio State = MCG 10 > MCW = UMass 6.67 > LSU = NGMC 3.33 > Henry Ford = ETSU = Wayne State 0** (Ann Arbor 0, not ranked). 2026-10-21: "UMass research is 10" -> **Tufts = Ohio State = MCG = UMass 10 > MCW 6.67 > LSU = NGMC 3.33 > Henry Ford = ETSU = Wayne State 0**. **What a research 10 means (Barath, 10/21): resources, protected time and support are all present.** Still 4 tiers. When a tier merges or is added, re-space all tiers evenly.
  - Notion stores Clinical, Research and the Teaching/Research composite in separate columns.
- **Field Preference**: future salary and job-finding potential given his visa status. Four tiers, spaced evenly (revised 2026-10-07; Barath: "make MCW, NGMC, ETSU the same field preference score"): Heme/Onc 10 > Critical Care, including pure CCM, PCCM and ID/CCM Combined, 6.67 > ID with an optional Critical Care year 3.33 (Tufts only) > plain ID 0. Heme/Onc is strictly above Critical Care, not tied. If Barath moves a specialty between tiers, re-space all tiers evenly.
- **Order = main score only (2026-10-19, Barath "arrange based on score pls").** The bottom-five re-ordering below is RETIRED (`BOTTOM_N = 0` in rebuild.py) and kept for history only. MDA regret no longer affects ranks.
- **Not ranked (2026-10-19):** Ann Arbor ("remove ann arbor from scoring but keep it in table saying not ranked"). It lives in `NOT_RANKED` in rebuild.py, is left out of every score, rank, robustness run and audit, and shows as "Not ranked" in tables. Notion: Claude-based Rank empty, note at the top of Notes. If removing a program empties a tier in any category, re-space that category evenly (Barath: "rescale all categories if mismatch occurs"); on 10/19 no category needed it.
- **Bottom five (2026-10-09, retired 2026-10-19)**: the programs ranked #6–10 by the main formula are re-ordered among themselves by **0.267 x Field + 0.40 x Geography + 0.333 x MD Anderson regret** only. Barath first said "I will weigh Heme/Onc and geography as the highest. Everything else doesn't matter to me" (Field 40 / Geography 60), then added MDA regret at one-third, with Field and Geography sharing the other two-thirds in their 40/60 ratio.
  - **MDA regret**: how much he'd regret matching there instead of MD Anderson leukemia, stored as "MDA Regret %" in Notion. Answers: LSU 20 and UMass 20 (10/10), Henry Ford "20–30%" (25 used), NGMC 40, ETSU 60, Wayne State 100, Ann Arbor 100. Scored 0–10 by spreading his values evenly (least regret 10, most regret 0). No answer = neutral 5, so ask for the regret % of any program near the #5/#6 line (all programs near the line now have one).
  - **Membership is recomputed on every run from the main score.** Henry Ford sits on the #5/#6 line (Barath: "Henry Ford may end up moving to the top if any of the programs in the top five score lower"). If a top-five program drops below it, Henry Ford moves up and that program is re-scored in the bottom five.
  - They always stay below the top five. Exact bottom-five ties fall back to the main score (his choice: Wayne State 3.257 over Ann Arbor 2.468, both 4.000). Code: rebuild.two_tier_order.
- **Geography**: Barath's location tiers spaced evenly 0 to 10. Current (2026-10-19: Ohio State "Geography score of 10"; before that, 10/13: "Columbus and Boston in one group, Milwaukee alone, New Orleans and Gainesville together"): Michigan (Henry Ford, Ann Arbor, Wayne State) = Columbus (Ohio State) 10 > Boston area (Tufts, UMass Chan) 6.67 > Milwaukee (MCW) = New Orleans (LSU) = Gainesville (NGMC) 3.33 > Augusta (MCG), Johnson City (ETSU) 0. (2026-10-21: "mcw geo is 2.5, rearrange scoring": Milwaukee joined the New Orleans/Gainesville tier and the 4 remaining tiers were re-spaced; before that Boston 7.5, Milwaukee 5, New Orleans/Gainesville 2.5.) Metro status (Indian community, nightlife, transit, airport) and distance to his girlfriend near Detroit are already reflected in this order. If Barath moves a city between tiers, re-space all tiers evenly rather than just editing one value.
- **Culture**: a composite, because Barath counts call and moonlighting as part of a program's culture. Culture = 0.625 x interview read + 0.25 x 24-hour call + 0.125 x moonlighting. On 2026-10-06 Barath removed leave and EMR ("Can we remove this leave policy from this equation? And the EMR."); the remaining three were rescaled in proportion from 45/18/9. Vacation days and EMR stay in Notion as reference data only and are never scored.
  - Interview read: 2.5 points each for liking the PD, 2+ faculty, the fellows, the coordinator. An item he feels neutral about ("didn't like, didn't dislike") or could only partly judge (met just one faculty member, whom he liked) gets half credit, 1.25, the same as any other unknown. An item that can't exist (no fellows yet at a new program, e.g. NGMC's first cohort) was a neutral 1.25 from 2026-10-06; under the no-neutral rule Barath set NGMC's to **0** on 2026-10-13. For any future case, ask him.
  - 24-hour call: favorable 10 only if fellows take no call at all; unfavorable 0 if any call exists, home/pager call included (Barath, 2026-10-02: "the fact that the call exists itself is unfavorable"). A separate night-float system where fellows take no call counts as favorable (MCW, confirmed 2026-10-02; Ann Arbor has no call after 7 PM). Exception (2026-10-06): light call of no more than one day a week, which Barath called "bearable", counts as favorable (Tufts).
  - Moonlighting: Yes 10, No 0.
  - Anything unknown or not yet assessed, including the interview read before the interview happens, is a neutral 5. Never carry a pre-interview guess as a real score.

## Verify every input with Barath, program by program

Barath's explicit instruction (2026-09-29): do not rely on Notion values alone. Notion data has drifted and held placeholders before. When rescoring or rebuilding, walk through each program individually, one program per round, and confirm its Clinical and Research scores, interview read (as a pick-which-you-liked list of PD, faculty, fellows, coordinator), 24-hour call and moonlighting with him, showing the current Notion value as the default. Field and Geography follow the fixed rules above, so state them for confirmation rather than asking open-ended. Show him the resulting table for approval before writing anything to Notion.

## Confirmed inputs snapshot (updated 2026-10-19)

A dated reference copy only. The live values are in Notion and win on any difference. Neutral = not yet known, counts as 5. Pending values are tracked in the "Still to be decided" checklist of the latest Legend section (mirrored in fellowship-rank-analysis/TBD.md on GitHub); show that checklist when Barath asks what's still undecided.

Vacation days and EMR (only Wayne State/DMC is bad, Cerner/Oracle Health) are kept as reference and are not scored.

| Rank | Program | Clinical | Research | Field | Geography | Interview read | 24-hr call | Moonlighting | Culture | Score |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Tufts | 10 | 10 | 3.33 (optional CCM year; Tufts ID PD: ~5% of grads go to ID critical care. The 1-year CCM is a separate application; alumni origins not verified) | 6.67 (10/21 re-spacing; was 7.5) | 10 (all four, 10/6) | Favorable (≤1 day/week, "bearable") | No (contract: visa holders can't moonlight) | 8.75 | 7.356 |
| 2 | Ohio State Wexner (added 10/13) | 10 | 10 | 0 (10/19: plain ID; was 3.33) | 10 (10/19: Columbus joins Michigan; was 7.5) | 8.75 PROVISIONAL (Barath 10/13: PD, faculty, fellows assumed nice; coordinator neutral; verify 10/28) | Favorable PROVISIONAL | No (assumed) | 7.96875 | 7.153 |
| 3 | UMass Chan | 6.67 | 10 (10/21: "UMass research is 10"; was 6.67) | 0 (plain ID; Barath 10/16 "same as Ann Arbor", after briefly 3.33 for the Brown CCM grad) | 6.67 (10/21 re-spacing; was 7.5) | 10 (all four; PD 10/12, faculty, fellows, coordinator liked 10/16) | Favorable (7–8 weekends/yr split among 7 fellows; Barath 10/16 "keep it favorable, we'll see") | No (not possible; 10/12) | 8.75 | 5.941 |
| 4 | MCW | 6.67 | 6.67 (10/19: "same as MCG"; was 3.33) | 6.67 | 3.33 (10/21: "mcw geo is 2.5" = joins New Orleans/Gainesville tier, re-spaced; was 5) | 5 (fellows, coordinator; PD not liked 10/7, faculty not liked 10/12) | Favorable (separate night float) | No | 5.625 | 5.726 |
| 5 | MCG | 3.33 ("same as LSU", 10/12; was 6.67) | 10 (10/20; was 6.67) | 10 | 0 | 6.25 (fellows, coordinator, faculty half credit; PD not liked 10/7) | Unfavorable (call every weekday, sometimes weekends; 10/10) | Yes | 5.15625 | 5.714 |
| 6 | Henry Ford Providence | 0 | 0 | 10 | 10 | 2.5 (fellows only; revised 10/6) | Unfavorable (home call every weekday, sometimes weekends; 10/10) | No | 1.5625 | 5.057 |
| 7 | LSU New Orleans | 3.33 ("same as ETSU", 10/9) | 3.33 | 10 | 3.33 (10/21 re-spacing; was 2.5) | 5 (faculty, fellows; PD and coordinator not liked) | Unfavorable (home call M–F 24h + ~2 weekends/month during 6–8 F1 inpatient months; confirmed in 10/9 interview recordings) | No (manual: J-1 may not moonlight; 10/9) | 3.125 | 4.962 |
| 8 | NGMC | 0 | 3.33 | 6.67 | 3.33 (10/21 re-spacing; was 2.5) | 5 (PD, coordinator; faculty NOT liked 10/13; fellows 0 since no fellows exist yet) | Unfavorable (10/21: Barath "these ppl wont follow the acgme rules"; 10/19 was favorable) | No (confirmed 10/19) | 3.125 | 3.547 |
| 9 | ETSU | 3.33 | 0 | 6.67 | 0 | 7.5 (PD, faculty, fellows liked; coordinator not liked, confirmed 10/13) | Favorable (10/21, after meet-and-greet detail: ID call is home pager only, ICU is 12-h shifts; 10/13 was unfavorable) | No (visa holders can't moonlight; chief fellow 10/12) | 7.1875 | 3.479 |
| 10 | Wayne State | 0 (10/19: "clinic 0"; was 3.33) | 0 (10/20; was 10) | 0 | 10 | 0 (10/19, pre-interview call by Barath; revisit after 10/27) | Unfavorable (10/19, pre-interview) | No (10/19) | 0 | 2.290 |
| — | Ann Arbor | 0 | 0 | 0 | 10 | 2.5 (coordinator only; PD not liked 10/7) | Favorable (no call after 7 PM) | No | 4.0625 | **Not ranked** (10/19) |

2026-10-21 (later): NGMC call unfavorable, ETSU call favorable; NGMC 3.547 and ETSU 3.479 stay #8/#9 (0.068 apart). 2026-10-21: UMass research 10 and the Geography re-spacing put UMass #3 (5.941), MCW #4 (5.726), MCG #5 (5.714); MCW vs MCG is 0.012 apart. 2026-10-20: MCG research 10 and Wayne State research 0 (Barath, after the PubMed screens and faculty-page check). MCG moves to #4 (5.714), Wayne State to #10 (2.290); closest call is now MCG vs UMass (#4/#5, 0.166). Since 2026-10-19 the order is the main score only (35/25/22.9/17.1, teaching 50/50). Closest call: MCG vs Henry Ford (#5/#6, 0.075; Geography +3% flips it). Wayne State fell to #8 on 10/19 (Clinical 0, Culture 0, pre-interview). Superseded note from before 10/19: ranks 7–11 (11 programs since 10/13) came from the bottom-five formula (Field 26.7 / Geography 40 / MDA regret 33.3): LSU 7.000, NGMC 5.279, Wayne State 4.000, Ann Arbor 4.000 (tie; main score decides), ETSU 3.445. NGMC call favorable since 10/19 (main score 3.785, rank unchanged). The Score column is the main-formula score (35/25/22.9/17.1, teaching 50/50) for reference. After the 10/16 UMass interview, UMass is #3 (6.131); the closest call is MCG vs Henry Ford (#5/#6, 0.075 apart; a 3% rise in the Geography weight flips it). UMass vs MCW (#3/#4) flips if the Field weight rises 25%.

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

## J-1 assumption (Barath, 2026-10-13)

"Assume all programs I interview at have J-1." Treat J-1 sponsorship as available at every interviewing program; don't flag it as a pending item or ask about it. (Moonlighting is still asked/scored separately; J-1 usually means no moonlighting.)

## No neutral values by the end (standing rule, Barath 2026-10-13)

"At the end of the day, there should be no neutral values in the whole table." Neutral 5s and neutral 1.25 read items are placeholders only, never final answers. Every rescore, `python3 rebuild.py` prints a **NEUTRAL VALUES LEFT** audit (`neutral_audit()`); show its count in the reply and list the items, and keep chasing them (ask after each interview, ask Barath directly for anything that doesn't need an interview). When an item is resolved for a read sub-part, remove it from `NEUTRAL_READ_ITEMS` in rebuild.py. The list is not certified until the audit says 0. This includes MDA regret % for programs in the top five (only used if they fall to the bottom five) and items that can't exist: ask Barath how he wants those scored rather than leaving them at 1.25 (NGMC fellows → 0, 10/13).

## Final check before certifying the rank list (agreed 2026-10-06)

After the last interview (Ohio State, 10/28; Wayne State 10/27) and before the Nov 18 deadline, run these in order:
0. **Zero neutral values and no provisional values:** the neutral audit in rebuild.py must report 0, and every value Barath said to "assume" before an interview (Ohio State read, call, moonlighting; UMass call was confirmed 10/16) must be confirmed or replaced from the interview.
1. **Fresh gut order first:** Barath writes his gut ranking 1 to 10 **before** seeing any model scores, so the model can't anchor him. Save it to the My Rank column and set MY_RANK_CURRENT = True.
2. **Blind re-scoring:** ask for Teaching/Research (and the interview read items) for all 10 programs **without** showing the old values. If any score moves by more than 1 from the stored value, discuss it, then rerun the model.
3. **Regret test:** for every FRAGILE adjacent pair (also Tufts vs Ohio State) from robustness.py, plus every program where the model and the fresh gut order differ by 3 or more places, ask "If you matched at A instead of B, which would you regret more?" His answer sets the final order for that pair. Record each answer in the Legend.
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
