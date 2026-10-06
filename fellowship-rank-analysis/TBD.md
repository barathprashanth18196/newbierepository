# Rank list: values still to be decided

Mirror of the "Still to be decided" checklist on the Notion Legend page, which is the source of truth. Every input below currently counts as a neutral 5 in the Claude based Rank. Update the value and rerun `python3 rebuild.py` as each one resolves. Mirrored as a checklist at the end of the latest numbered section (26) on the Notion Rank List Scoring Legend page. Last updated 2026-10-06.

| Program | What's pending | Resolves when | Current rank |
|---|---|---|---|
| LSU New Orleans | Moonlighting | Ask at 10/9 interview | 3 |
| UMass Chan | Interview read, 24-hour call, moonlighting | Interview 10/16 | 6 |
| Wayne State | Interview read, 24-hour call, moonlighting | Interview 10/27 | 8 |
| ETSU | 24-hour call: in-house call on ICU months (4 of 12), unclear whether true 24-hour or night float | Post-interview fellows' meet-and-greet (interview itself done 9/18) | 9 |
| ETSU | Moonlighting | Post-interview fellows' meet-and-greet | 9 |

No pending inputs: MCW, MCG, NGMC, Ann Arbor, Henry Ford, Tufts.

## Close calls to recheck once the above resolves (as of 10/6, after leave and EMR were removed from Culture)

- **Tufts vs MCW vs LSU:** Tufts 7.764, MCW 7.545, LSU 7.471. MCW and LSU swap #2/#3 under ±10% weights. LSU moonlighting Yes alone adds only about +0.06 (7.530, still just behind MCW's 7.545); a higher 10/9 interview read (7.5 to 10) adds about +0.15 and would put LSU back at #2.
- **NGMC vs Wayne State vs ETSU** (5.105 / 5.027 / 5.000 after NGMC's fellows item went neutral 10/6): close, but not an exact tie, so no tiebreak. Wayne State's and ETSU's pending call/moonlighting answers will decide it.

## Standing reminders (raise at the start of every rank-list chat)

- **Bottom-five weighting:** Barath may provide a new weighting for the bottom five (UMass Chan, NGMC, Wayne State, ETSU, Ann Arbor as of 10/6). Waiting on him; don't invent one.
- **Culture still unfilled:** Tufts (complete 10/6), LSU (moonlighting), UMass Chan (read, call, moonlighting), Wayne State (read, call, moonlighting), ETSU (call, moonlighting; ask at the post-interview fellows' meet-and-greet, interview done 9/18). Complete: MCW, MCG, NGMC, Ann Arbor, Henry Ford (10/2).
- ~~Recheck under the clarified call rule~~ Done 10/2: MCW uses a separate night-float system, Ann Arbor has no call after 7 PM. Both stay favorable.
- **Culture formula (10/6):** leave and EMR removed at Barath's request. Culture = 62.5% interview read + 25% call + 12.5% moonlighting. Vacation days and EMR are reference only.
- **NGMC fellows (10/6):** no fellows exist (first cohort), so the fellows item is a neutral 1.25. Interview read 8.75, no longer pending.
- **Model vs gut (10/6, robustness.py check 8):** Spearman 0.47 against the My Rank column in Notion. Gaps of 3+ places to discuss: LSU (model #3, gut #8), MCW (#2 vs #6), Henry Ford (#5 vs #1), ETSU (#9 vs #5), UMass (#6 vs #3).
- **Every rescore:** run `python3 robustness.py` and add a Robustness block to the reply and the Legend section.
- **My Rank is out of date (Barath, 10/6):** the gut check is off until he gives a fresh gut order.
- **Final check after the last interview (10/27), before Nov 18:** (1) a fresh gut order before he sees any scores, (2) blind re-scoring of Teaching and interview reads, (3) a regret test on every fragile pair and every big model-vs-gut gap, (4) rerun robustness.py and certify.
