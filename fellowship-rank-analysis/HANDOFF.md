# Handoff: Barath's fellowship rank list (2026-10-27)

**Where we stopped:** All scoring is current through Wayne State's pre-interview inputs. Branch `claude/umass-interview-debrief-o32ex1`; everything is committed and pushed (last commit 0c9b787). No PR has been opened yet.

**Order now:** Tufts 7.356, Ohio State 7.286, Wayne State 5.858, MCW 5.726, MCG 5.714, UMass Chan 5.358, LSU 4.200, ETSU 3.479, UMass Baystate 2.574. NGMC and Ann Arbor are shown but not ranked; Henry Ford is removed. Neutral values left: 3 (Wayne State's PD, faculty and fellows read items).

**Next action:** Wayne State interviewed 10/27. Pull its recording with Plaud `list_files` (date 2026-10-27), read the whole transcript, and post a debrief on the Notion Wayne State page (`3d650330e23b813fbd75fe7491447462`). Ask Barath for his read of the PD, faculty and fellows (the coordinator is already "not liked") and for the 24-hour call (pre-interview: unfavorable). Clinical 6.67 is provisional ("same as mcw for now"), so confirm it. Then update `NEUTRAL_READ_ITEMS` and the Wayne State tuple in `fellowship-rank-analysis/rebuild.py`, and run `python3 fellowship-rank-analysis/rebuild.py`.

**After every rescore, update all four places:**
- `rebuild.py`
- The Notion Interview Tracker properties: Clinical, Research, Teaching/Research, Field Preference, Geography, Culture, 24-Hour Call Policy, Claude-based Rank. Notion writes are pre-approved, so don't ask.
- The snapshot table and dated line in `fellowship-rank-analysis/fellowship-rank-list-preferences/SKILL.md`, plus an entry in `TBD.md`.
- The Rank Board artifact https://claude.ai/artifact/9PD9iRMe48Y3k2ewkEJuGt: pass `url` on the first publish in a new session. Its source copy is `fellowship-rank-analysis/rank-board.html`. Re-rank and reorder the rows.

**Reply rules:**
- Always show the ENTIRE scoring table, with Program as the first column.
- American English, a little sarcasm, smiley faces.
- Start every message with the timestamp marker.

**How to keep the Fellowship Rank Board going** (https://claude.ai/artifact/9PD9iRMe48Y3k2ewkEJuGt, v21):

1. **Start each new session** with Artifact `action: "read"` on that URL. It returns the saved full page; treat that as the live version, since Barath may have edited it. Copy it to the scratchpad. `fellowship-rank-analysis/rank-board.html` is the repo copy, current as of v21.
2. **Publish** with Artifact `file_path` set to the scratchpad copy plus `url` set to the board URL. Without `url` you get a new artifact. Don't pass `icon`. After each publish, copy the file back to `fellowship-rank-analysis/rank-board.html` and commit it.
3. **Page layout:** one `<table>` with a sticky Program column and sticky header. Column groups:
   - Program
   - Teaching & research: Clinical, Research, Papers kept, Division-led, Trials, Faculty publishing, CCM research (`td.ccm`), Electives Y1/Y2 (`td.elec`), Teaching
   - Field & place: Field, Geography
   - Culture: Interview read, 24-hr call, Moonlighting, Culture
   - Total (`td.total`)
   - Money: PGY-4 salary (+3%), Take-home, Rent 30%, Max rent
   - Tamil Sangam (`td.tam`)
4. **Rows** are `<tr><td class="prog"><span class="rk">N</span><b>Name</b><small>…</small></td>…</tr>`. Unranked rows use `<tr class="off">` with rank "—".
   - Edit rows with a small Python script keyed on `<b>Name</b>`, and assert every replacement actually happened.
   - After a rescore, change the cell values, the `rk` numbers and the row order to match `rebuild.py` output.
   - Cell classes: `prov` = provisional, `fav`/`unfav` = call, `est` + `*` = estimated salary.
5. **Notes** are the `.notes` `<p>` paragraphs under the table. They cover the formula, research counts, CCM research, electives sources, money assumptions and estimate footnotes. Update the matching note when a column's meaning changes.
6. **Money:** compute with `fellowship-rank-analysis/takehome.py` `month(state, salary*1.03, city)`, using salaries from `pgy4_salaries_2026-10-25.json`. Then: rent = 30% of take-home, max rent = take-home − $3,000.
7. **Electives cells** hold numbers only ("2.5 / 7", "—" when the program gave no number). Details go in the notes and in `electives_by_program_2026-10-27.md`.

**Upcoming:**
- **Ohio State interview 10/28.** Its read and call (10 / favorable) are assumptions; re-score from the Plaud recording. Fill its electives cell, now "? / ?", and confirm the salary (2025-26 figure).
- Electives counts live in `electives_by_program_2026-10-27.md`. The board shows numbers only, never the word "research" in the cell.

**Open questions:**
- Baystate ID faculty-publishing count: hospital sites are blocked from the cloud container; needs Barath's Mac (`claude rc`).
- Tufts moving and housing stipend amounts: ask Tufts GME at 617-636-6352.

**Autostart:** yes
