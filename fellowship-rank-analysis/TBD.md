# Rank list: values still to be decided

Mirror of the "Still to be decided" checklist on the Notion Legend page, which is the source of truth. Every input below currently counts as a neutral 5 in the Claude based Rank. Update the value and rerun `python3 rebuild.py` as each one resolves. Mirrored as a checklist at the end of the latest numbered section (26) on the Notion Rank List Scoring Legend page. Last updated 2026-10-19.

| Program | What's pending | Resolves when | Current rank |
|---|---|---|---|
| Wayne State | Scored 10/19 before the interview (Clinical 0, Culture 0); revisit after 10/27 | Interview 10/27 | 8 |
| UMass Chan-Baystate ID (new 10/15) | BOOK interview date in Thalamus (first-come); Clinical, Research, Geography (Springfield), Field (CCM year?), MDA regret %; culture after interview | Interview TBD (virtual) | not yet scored |
| Ohio State (new 10/13) | Verify provisional culture (read 8.75, call favorable, moonlighting No); coordinator | Interview 10/28 (virtual) | 2 |

No pending inputs: UMass Chan (10/16), MCW, MCG, NGMC, Henry Ford, Tufts, LSU (moonlighting No per the 2026 manual, 10/9), ETSU (10/13; coordinator confirmed not liked). Ann Arbor: not ranked (10/19). MDA regret % no longer affects ranks (bottom-five formula retired 10/19).

## Close calls to recheck once the above resolves (as of 10/9, after MDA regret was added)

- **#5/#6 line, LSU vs Henry Ford** (main 4.360 vs 3.767): flips if the Teaching weight drops 20%. Henry Ford would move to #5, and LSU would be re-scored in the bottom five (neutral regret 5 → 5.333 → #7). **Need LSU's and UMass's MDA regret %.**
- **ETSU vs Wayne State / Ann Arbor** (bottom-5 score 3.556 vs 4.000): flips if the regret weight rises from 33% to about 39%.
- **Wayne State vs Ann Arbor** (4.000 each): exact tie, settled by the main score.

## Standing reminders (raise at the start of every rank-list chat)

- ~~**Bottom-five weighting**~~: resolved 10/9. Ranks 6–10 are re-ordered by Field 26.7% + Geography 40% + MD Anderson regret 33.3%. Regret: Henry Ford 25%, NGMC 40%, ETSU 60%, Wayne State 100%, Ann Arbor 100%. Order: Henry Ford, NGMC, Wayne State, Ann Arbor, ETSU. Membership is recomputed every run, so Henry Ford moves up if a top-five program falls below it.
- **Culture still unfilled:** Wayne State (read, call, moonlighting). Complete: UMass (10/16), ETSU (10/13), MCW, MCG, NGMC, Ann Arbor, Henry Ford (10/2), Tufts (10/6), LSU (10/9).
- ~~Recheck under the clarified call rule~~ Done 10/2: MCW uses a separate night-float system, Ann Arbor has no call after 7 PM. Both stay favorable.
- **Culture formula (10/6):** leave and EMR removed at Barath's request. Culture = 62.5% interview read + 25% call + 12.5% moonlighting. Vacation days and EMR are reference only.
- **NGMC fellows (10/6):** no fellows exist (first cohort), so the fellows item is a neutral 1.25. Interview read 8.75, no longer pending.
- **Model vs gut (10/6, robustness.py check 8):** Spearman 0.47 against the My Rank column in Notion. Gaps of 3+ places to discuss: LSU (model #3, gut #8), MCW (#2 vs #6), Henry Ford (#5 vs #1), ETSU (#9 vs #5), UMass (#6 vs #3).
- **Every rescore:** run `python3 robustness.py` and add a Robustness block to the reply and the Legend section.
- **My Rank is out of date (Barath, 10/6):** the gut check is off until he gives a fresh gut order.
- **Final check after the last interview (10/27), before Nov 18:** (1) a fresh gut order before he sees any scores, (2) blind re-scoring of Teaching and interview reads, (3) a regret test on every fragile pair and every big model-vs-gut gap, (4) rerun robustness.py and certify.
- **PD read (10/7):** Barath didn't like the PD at MCW, LSU, MCG, Henry Ford or Ann Arbor. PD credit removed; the order is unchanged.
- **Field re-spaced (10/7):** MCW, NGMC and ETSU now share one Critical Care tier (6.67); Tufts moves to 3.33. New order: Tufts, LSU, MCW, MCG, Henry Ford, UMass, ETSU, Wayne State, NGMC, Ann Arbor.
- **Teaching split + 0–10 spread + Field = Geography (10/9):** Teaching = 65% Clinical + 35% Research. Clinical 10/8/6/4 spread to 10/6.67/3.33/0. Research tiers: Tufts 10, MCG 7.5, UMass 5, MCW/LSU/NGMC/Ann Arbor 2.5, Henry Ford/ETSU/Wayne State 0. Weights now 54.4/20.1/16.1/9.4. New order: Tufts, MCG, MCW, UMass, LSU, Henry Ford, Wayne State, NGMC, ETSU, Ann Arbor. NGMC vs ETSU is an effective tie (Geography tiebreak favors NGMC).
- **Always update Notion and the skill on every change (10/9).**
- **LSU interviewed 10/9:** debrief from all 4 Plaud recordings is on the LSU Notion page. No score change. Call stays unfavorable (LSU fairness check done). BMT confirmed at Our Lady of the Lake, Baton Rouge. Waiting on Barath: post-interview read (PD/coordinator flags), clinical teaching, MDA regret % for LSU.
- **LSU (10/10):** MDA regret 20%; all other LSU scores kept as is (PD/coordinator not liked, clinical 6). No rank change.
- **Tufts CCM year (10/10):** ID PD's slide says ~5% of grads go into ID critical care. The 1-year CCM fellowship is a separate application; its alumni origins were not verifiable online. To do: email the CCM coordinator or ID PD.
- **Call-frequency fairness check (10/10):** Henry Ford and MCG have call every weekday, sometimes weekends, so both stay unfavorable. LSU is done (unfavorable). NGMC: frequency TBD (ask 10/19); stays unfavorable for now. Even if NGMC qualified, no rank change.
- **UMass MDA regret 20% (10/10)**, same as LSU. No live rank change.
- **What-ifs (10/10, not adopted):** Teaching 40% or 35% (others rescaled in proportion) both give Tufts, MCG, MCW, Henry Ford, LSU, UMass, NGMC, Wayne State, Ann Arbor, ETSU. Decision pending: keep 54.4% or adopt 40%/35%.
- **MCG clinical = LSU (10/12):** 6.67 → 3.33. MCG 6.281 → 5.100, #2 → #3; MCW #2. New fragile pair: MCG vs UMass (#3/#4, 0.112 apart); UMass's 10/16 answers decide it.
- **Teaching 35% adopted (10/12):** weights 35 / 28.7 / 22.9 / 13.4. Order: Tufts, MCW, Henry Ford, MCG, LSU | UMass, NGMC, Wayne State, Ann Arbor, ETSU. Fragile: Henry Ford vs MCG (#3/#4, Geography −5% flips); LSU vs UMass at the line (Field −11%).
- **MCW faculty not liked (10/12):** read 7.5 → 5, Culture 5.625, score 5.637. Still #2; MCW vs Henry Ford is now 0.268 apart.
- **Field capped at 25% (10/12):** weights 35 / 25 / 22.9 / 17.1. Order: Tufts, MCW, MCG, Henry Ford, UMass | LSU, NGMC, Wayne State, Ann Arbor, ETSU. Near tie: MCG vs Henry Ford (0.0009). UMass vs LSU at the line: 0.032.
- **Teaching split 50/50 (10/12):** clinical and research each 17.5% of the total. Order: Tufts, MCW, MCG, Henry Ford, LSU | UMass, NGMC, Wayne State, Ann Arbor, ETSU. LSU vs UMass at the line: 0.012 apart (closest call).
- **Elaborate scores always (10/12):** every reply that shows scores or ranks uses the full elaborate breakdown (split tables, raw → points, Clinical/Research, Culture sub-parts, line row, bottom-five regret math, Changed line, Robustness). Short version only when Barath asks for it.
- **UMass PD liked + moonlighting not possible (10/12):** read 6.25, moonlighting No, Culture 5.156, score 4.641. UMass crosses to #5 (0.014 ahead); LSU drops to #6 (bottom-five 7.000). UMass after 10/16: best #4, worst #6.
- **ETSU meet-and-greet (10/12):** moonlighting No (visa), Culture 5.9375, score 3.266, still #10. Call waits on Barath (favorable 3.479 / unfavorable 3.052; #10 either way). Debrief on the ETSU Notion page; Plaud tracker updated.
- **ETSU call unfavorable (10/13):** Barath: 24-h call M–F on ID + 1 weekend/month. Culture 4.6875, score 3.052, still #10. ETSU fully scored; coordinator confirmed not liked (read 7.5).
- **No neutral values by the end (Barath, 10/13):** standing rule. `rebuild.py` prints a NEUTRAL VALUES LEFT audit; the list isn't certified until it says 0. As of 10/13, 11 left: UMass faculty/fellows/coordinator read + call (10/16); Wayne State read, call, moonlighting (10/27); NGMC fellows read item (no fellows exist, Barath to decide how to score); MDA regret % for Tufts, MCW, MCG.
- **NGMC fellows item 0 (10/13):** read 8.75 → 7.5, Culture 4.6875, score 4.052, still #7. Neutral values left: 10 (UMass 4, Wayne State 3, MDA regret % for Tufts/MCW/MCG).
- **Ohio State Wexner ID added (10/13):** interview 10/28, virtual. Plain ID (Field 0 unless a CCM year exists), Epic, 15 vacation days. Not in the model until Barath gives Geography, Research and MDA regret %. Final check now starts after 10/28.
- **Research tiers re-spaced (10/13):** MCG = UMass. Tufts 10 > MCG, UMass 6.67 > MCW, LSU, NGMC, Ann Arbor 3.33 > Henry Ford, ETSU, Wayne State 0. No rank change. Fragile: MCG vs Henry Ford (0.075), Henry Ford vs UMass (0.123). J-1 assumed at every program (Barath).
- **Ohio State scored, Geography regrouped (10/13):** Michigan 10 > Boston area = Columbus 7.5 > Milwaukee 5 > New Orleans = Gainesville 2.5 > Augusta, Johnson City 0 (NGMC 5 → 2.5). Ohio State: clinical 10, research 10, Field 3.33, Geography 7.5 → 6.905, #2. Ranks 7–11 now re-ordered by the bottom-five formula (Barath to confirm bottom five vs six). Neutral values left: 14. Division Director Susan Koletar (ACTU PI); PD Mohammad Sobhanie.
- **Ohio State provisional culture (10/13):** Barath assumes PD, faculty, fellows nice, call favorable, moonlighting No until 10/28. Score 7.413, #2, 0.133 behind Tufts. Tufts #1 in only 64% of Monte Carlo runs with tier noise. Barath likes Susan Koletar (Division Director, ACTU PI); questions on the Ohio State Notion page.
- **UMass call favorable, provisional (10/13):** Culture 6.406, score 5.147, #4 (0.015 ahead of MCG, the closest call). MCG 4→5, Henry Ford 5→6. Neutral values left: 11.
- **NGMC faculty not liked (10/13):** read 5.0, Culture 3.125, main 3.357; still #8 (bottom-five 5.279). Calendar synced: Ohio State 10/28 and the 11/18 rank list deadline added; 10/28 overlaps the HS Gainesville clinical day (arrange coverage).
- **Baystate ID added (10/15):** Thalamus invite (PD Armando Paez, APD Durane Walker), virtual, date not yet booked. Not scored yet. Comparison vs DMC/Wayne State for physician-scientist and ID-CCM is on both Notion pages.
- **UMass interviewed 10/16 (Legend 58):** both Plaud recordings read in full; debrief on the UMass page; Plaud tracker updated. Barath: faculty, fellows, coordinator liked (read 10); call favorable kept (7–8 weekends/yr, "we'll see"); Field 0 → 3.33 (a 2026 grad did 1-yr CCM at Brown). Culture 8.75, score 6.381, #4 → #3; MCW #4. Closest call now MCG vs Henry Ford (0.075, Geography +3%). Neutral values left: 8. Follow-ups by email: Theodoropoulos, MICU electives, Worcester PCCM, gonorrhea vaccine trial, BMT research, Moormann.
- **UMass research → 10 (10/16, Legend 59):** Barath moved UMass into the top research tier with Tufts and Ohio State (still 4 tiers, no re-spacing). Teaching 8.335, score 6.963, still #3. No rank change.
- **Ann Arbor research → 0 (10/16, Legend 60):** lowest tier with Henry Ford, ETSU, Wayne State (still 4 tiers). Main score 3.567 → 2.985; still #10 (bottom-five 4.000, ties Wayne State, main score decides). No rank change.
- **UMass Field back to 0 (10/16, Legend 61):** Barath "same as Ann Arbor" (plain ID). Score 6.963 → 6.131, still #3. UMass vs MCW now flips with Field weight +25%; add it to the final regret test.
- **NGMC call favorable (10/19, Legend 62):** Barath "no 24 hr calls" before the interview. Call 0 → 1, Culture 3.125 → 5.625, main score 3.357 → 3.785; still #8 (bottom-five 5.279 doesn't use Culture). Moonlighting No and 4 fellows/year confirmed. NGMC call-frequency item closed.
- **Research re-tiered, Ann Arbor not ranked, score-only order (10/19, Legend 63):** Wayne State research 0 → 10; MCW 3.33 → 6.67 and UMass 10 → 6.67 ("same as MCG"). Tiers: Tufts = Ohio State = Wayne State 10 > MCG = MCW = UMass 6.67 > LSU = NGMC 3.33 > Henry Ford = ETSU 0. Ann Arbor removed from scoring (kept in tables as "Not ranked"); no category needed rescaling. Bottom-five formula retired: order is the main score only. Teaching split stays 50/50 (60/40 previewed, not adopted). Order: Tufts 7.546, Ohio State 7.413, MCW 6.109, UMass 5.548, Wayne State 5.478, MCG 5.132, Henry Ford 5.057, LSU 4.772, NGMC 3.785, ETSU 3.052. Fragile: MCG vs Henry Ford (Geography +3%), UMass vs Wayne State (Geography +9%; Wayne State culture still neutral). Neutral values left: 4.
- **NGMC interviewed (10/19):** both Plaud recordings read in full; debrief at the top of the NGMC Notion page (local copy: ngmc_debrief_2026-10-19.md); Plaud tracker updated; Status Completed. Waiting on Barath: post-interview read (PD, faculty, coordinator) and clinical teaching. To-do: tell Dr. Deshmukh before the ranking meeting whether PCCM is his real choice.
- **Ohio State Field 0, Geography 10 (10/19, Legend 64):** plain ID (no optional CCM year) and Columbus joins the Michigan tier. Score 7.413 → 7.153, still #2. Tufts vs Ohio State now flips if the Field weight drops 40%; Ohio State vs MCW flips if Field rises 41%. No rescale needed.
- **Wayne State Clinical 0, Culture 0 (10/19, Legend 65):** Barath, pre-interview. Teaching 6.665 → 5.0, Culture 5.0 → 0 (read 0, call unfavorable, moonlighting No). Score 5.478 → 4.040, #5 → #8; MCG #5, Henry Ford #6, LSU #7. Neutral values left: 1 (Ohio State coordinator). Revisit after 10/27.
- 2026-10-21: **UMass Baystate ID (Springfield, MA)**: new interview offered. Not scored yet; needs Clinical, Research, Geography tier (Springfield vs Boston area), interview read, call, moonlighting, and interview date.
- 2026-10-25: Henry Ford removed from scoring and table; NGMC not ranked (shown like Ann Arbor). Ranked list is now 8 programs.
- 2026-10-25: UMass Baystate: PGY-4 $84,581 confirmed, optional CCM (Field 3.33), 4 weeks vacation. Still needs Clinical, Research, Geography (Springfield), read, call, moonlighting.
- 2026-10-25: UMass Baystate: Research 0, fellows read item 0, moonlighting No. Still needs Clinical, Geography (Springfield), PD/faculty/coordinator read, call.
- 2026-10-25: UMass Baystate Geography 3.33 (same tier as MCW/Milwaukee). Still needs Clinical, PD/faculty/coordinator read, call.
- 2026-10-25: LSU Geography 3.33 -> 0 (New Orleans joins Augusta/Johnson City). LSU 4.962 -> 4.200, still #6.
- 2026-10-25: UMass Baystate Clinical 3.33 ("same as mcg"); Teaching 1.665. Still needs PD/faculty/coordinator read and 24-hr call to score.
- 2026-10-25: UMass Baystate scored provisionally: read 7.5 assumed, call unknown (neutral). 3.193, #8 (fav call 3.407 / unfav 2.979, #8 either way). Wayne State #9. Confirm read and call after interview.
- 2026-10-25: Baystate 24-hr call unfavorable (2.979, #8). Ohio State coordinator liked -> read 10, 7.286, #2. Neutral values left: 0.
