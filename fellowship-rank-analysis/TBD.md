# Rank list: values still to be decided

Mirror of the "Still to be decided" checklist on the Notion Legend page, which is the source of truth. Every input below currently counts as a neutral 5 in the Claude based Rank. Update the value and rerun `python3 rebuild.py` as each one resolves. Mirrored as a checklist at the end of the latest numbered section (26) on the Notion Rank List Scoring Legend page. Last updated 2026-10-06.

| Program | What's pending | Resolves when | Current rank |
|---|---|---|---|
| UMass Chan | Faculty, fellows, coordinator read; 24-hour call (PD liked + moonlighting No in, 10/12) | Interview 10/16 | 5 |
| Wayne State | Interview read, 24-hour call, moonlighting | Interview 10/27 | 8 |

No pending inputs: MCW, MCG, NGMC, Ann Arbor, Henry Ford, Tufts, LSU (moonlighting No per the 2026 manual, 10/9), ETSU (10/13; coordinator confirmed not liked).

## Close calls to recheck once the above resolves (as of 10/9, after MDA regret was added)

- **#5/#6 line, LSU vs Henry Ford** (main 4.360 vs 3.767): flips if the Teaching weight drops 20%. Henry Ford would move to #5, and LSU would be re-scored in the bottom five (neutral regret 5 → 5.333 → #7). **Need LSU's and UMass's MDA regret %.**
- **ETSU vs Wayne State / Ann Arbor** (bottom-5 score 3.556 vs 4.000): flips if the regret weight rises from 33% to about 39%.
- **Wayne State vs Ann Arbor** (4.000 each): exact tie, settled by the main score.

## Standing reminders (raise at the start of every rank-list chat)

- ~~**Bottom-five weighting**~~: resolved 10/9. Ranks 6–10 are re-ordered by Field 26.7% + Geography 40% + MD Anderson regret 33.3%. Regret: Henry Ford 25%, NGMC 40%, ETSU 60%, Wayne State 100%, Ann Arbor 100%. Order: Henry Ford, NGMC, Wayne State, Ann Arbor, ETSU. Membership is recomputed every run, so Henry Ford moves up if a top-five program falls below it.
- **Culture still unfilled:** UMass Chan (faculty/fellows/coordinator read, call), Wayne State (read, call, moonlighting). Complete: ETSU (10/13), MCW, MCG, NGMC, Ann Arbor, Henry Ford (10/2), Tufts (10/6), LSU (10/9).
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
