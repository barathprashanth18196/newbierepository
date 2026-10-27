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

**Upcoming:**
- **Ohio State interview 10/28.** Its read and call (10 / favorable) are assumptions; re-score from the Plaud recording. Fill its electives cell, now "? / ?", and confirm the salary (2025-26 figure).
- Electives counts live in `electives_by_program_2026-10-27.md`. The board shows numbers only, never the word "research" in the cell.

**Open questions:**
- Baystate ID faculty-publishing count: hospital sites are blocked from the cloud container; needs Barath's Mac (`claude rc`).
- Tufts moving and housing stipend amounts: ask Tufts GME at 617-636-6352.

**Autostart:** yes
