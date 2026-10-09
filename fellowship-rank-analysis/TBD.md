# Rank list: values still to be decided

Mirror of the "Still to be decided" checklist on the Notion Legend page, which is the source of truth. Every input below currently counts as a neutral 5 in the Claude based Rank. Update the value and rerun `python3 rebuild.py` as each one resolves. Mirrored as a checklist at the end of the latest numbered section (26) on the Notion Rank List Scoring Legend page. Last updated 2026-10-06.

| Program | What's pending | Resolves when | Current rank |
|---|---|---|---|
| UMass Chan | Interview read, 24-hour call, moonlighting | Interview 10/16 | 6 |
| Wayne State | Interview read, 24-hour call, moonlighting | Interview 10/27 | 8 |
| ETSU | 24-hour call: in-house call on ICU months (4 of 12), unclear whether true 24-hour or night float | Post-interview fellows' meet-and-greet (interview itself done 9/18) | 7 |
| ETSU | Moonlighting | Post-interview fellows' meet-and-greet | 7 |

No pending inputs: MCW, MCG, NGMC, Ann Arbor, Henry Ford, Tufts, LSU (moonlighting No per the 2026 manual, 10/9).

## Close calls to recheck once the above resolves (as of 10/9, after the Teaching split)

- **NGMC vs ETSU** (3.136 vs 3.135): effectively tied; the Geography tiebreak would favor NGMC. ETSU's call/moonlighting answers will decide it.
- **Wayne State vs NGMC** (3.257 vs 3.136): flips with a 7% Field-weight increase. Wayne State's 10/27 answers can move it #7–9.
- **UMass** stays #4 whatever its 10/16 answers.

## Standing reminders (raise at the start of every rank-list chat)

- **Bottom-five weighting:** Barath may provide a new weighting for the bottom five (Henry Ford, Wayne State, NGMC, ETSU, Ann Arbor as of 10/9). Waiting on him; don't invent one.
- **Culture still unfilled:** UMass Chan (read, call, moonlighting), Wayne State (read, call, moonlighting), ETSU (call, moonlighting; ask at the post-interview fellows' meet-and-greet, interview done 9/18). Complete: MCW, MCG, NGMC, Ann Arbor, Henry Ford (10/2), Tufts (10/6), LSU (10/9).
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
