# Session handoff (2026-10-16)

Read this first in a new session, then load the `fellowship-rank-list-preferences` skill. Notion is the source of truth. This file is just a bridge between chats.

## Where things live

- **Live scores:** Notion Interview Tracker, data source `collection://0c47349b-53fa-4599-9325-80a711395c44` ("Claude based Rank" column).
- **Rules, history, pending values:** the Notion "Rank List Scoring Legend" page, https://app.notion.com/p/3d650330e23b814cbd7dd74457fd5872. The latest numbered section is **57** (NGMC faculty not liked; calendar synced, 10/13). Baystate was added 10/15. Re-check the page for the highest section number before appending the next one.
- **Plaud tracker:** "Interview Recordings (Plaud)", https://app.notion.com/p/3f550330e23b81c7a1b7ea73f297969d. Keep MD Anderson (9/29) on it.
- **Code** (this folder):
  - `rebuild.py`: inputs, formula and `neutral_audit()`.
  - `robustness.py`: 8 checks; check 8, the gut check, is off until a fresh gut order exists.
  - `montecarlo.py` and `analysis.py`: helpers.
  - `TBD.md`: pending items and the dated log.
- **Skill:**
  - Repo copy: `fellowship-rank-list-preferences/SKILL.md`.
  - Synced copy in the session's skills directory, if present.
  - After a rule change, remind Barath to re-upload the skill in claude.ai Settings.
- **Branch:** `claude/fellowship-rank-analysis-8i39ux`. Commit and push every change.

## Current list (unchanged since 10/13; Baystate unscored)

| # | Program | Score |
|---|---|---|
| 1 | Tufts | 7.546 |
| 2 | Ohio State (culture provisional until 10/28) | 7.413 |
| 3 | MCW | 5.524 |
| 4 | UMass Chan (read items + call provisional, now resolvable) | 5.147 |
| 5 | MCG | 5.132 |
| 6–11 | Henry Ford (5.057), then the bottom five re-ordered: LSU, NGMC, Wayne State, Ann Arbor, ETSU | |

Rerun `python3 rebuild.py` to confirm before showing anything.

## Do first: the UMass interview (done 10/16)

1. **Pull Plaud.** `list_files` for 10/16, then read the **entire** transcript of every UMass recording and say how much was read.
   - If Plaud hasn't transcribed a recording, use the `transcribe-audio` skill.
   - The earlier local sherpa-onnx setup lived in the old scratchpad and is gone.
2. **Write the Interview Debrief** at the top of the UMass Chan Interview Tracker page, in the skill's format (Henry Ford's page is the reference example).
3. **Answer the questions planned for this interview:**
   - Ann Moormann's research
   - The gonorrhea vaccine studies
   - Research potential in ID-BMT
   - The ID-CCM path, and whether Worcester has a pulm/CCM track and how research-heavy it is
   - Nicole Theodoropoulos
   - MICU electives
4. **Update the Plaud tracker** with every recording from 10/16: date, program mention, exact Plaud title and length. Don't paste audio links; they expire.
5. **Ask Barath for the inputs:**
   - Faculty, fellows and coordinator read: liked or not. Each currently counts as a neutral 1.25.
   - Confirm call. It's assumed favorable (10/13, provisional). Flag it if the recording contradicts this.
   - Moonlighting is already No, and the PD is already liked.
6. **Rescore and sync everything:**
   - `rebuild.py` and the NEUTRAL VALUES LEFT audit
   - `robustness.py`
   - Notion tracker, re-queried to verify
   - A new Legend section with the "Still to be decided" checklist carried forward
   - The skill's inputs snapshot
   - `TBD.md`, then commit and push
7. **Show the elaborate scores:**
   - One combined table of all programs: raw → weighted points for every criterion, plus a Bottom-5 score column.
   - A separate bottom-five table.
   - A "Changed:" line, a Robustness block, and the neutral-values count. No arrows.

UMass is fragile: it's #4, 0.015 ahead of MCG. Its read items and call decide #4 vs #5, and possibly #6.

## Still open after UMass

- **NGMC 10/19:** call frequency.
- **Wayne State 10/27:**
  - Interview read, call and moonlighting.
  - Confirm the 1-year DMC ID→CCM path; it could raise Field to 3.33.
- **Ohio State 10/28 (virtual):**
  - Verify the provisional culture (read 8.75, call favorable, moonlighting No) and the coordinator.
  - Arrange coverage for the HS Gainesville clinical day.
- **Baystate:**
  - Book the interview in Thalamus.
  - Get Barath's Clinical, Research, Geography (Springfield), Field (CCM year?) and MDA regret %.
- **Decisions Barath still owes:**
  - MDA regret % for Tufts, Ohio State, MCW and MCG
  - Bottom five vs bottom six
  - Optional research-tier changes (MCG up / Tufts down). Not applied.
  - Email Tufts about its CCM year.
- **Final check before Nov 18 (after 10/28):**
  - Zero neutral and zero provisional values
  - A fresh gut order
  - Blind re-scoring
  - Regret tests (Tufts vs OSU, UMass vs MCG, MCG vs HF)
  - Rerun robustness, then certify

## Standing rules (short version; the skill has the full text)

- Always update Notion and the skill.
- J-1 is assumed at every program.
- No neutral and no provisional values at certification.
- Re-space all tiers whenever tiers merge or are added.
- After each interview: Plaud, the full transcript, a debrief, the Plaud tracker, then ask for inputs.
- Barath likes replies with a little sarcasm and a smiley face.

## Side project (not Barath's list)

A friend's cardiology version lives outside this repo. Don't mix it with this data.

- Intake page: https://claude.ai/artifact/R9DrggcqiHsonXAMpJ3bt9. Its answers save to its own store, in the `intake` collection.
- Build guide: https://claude.ai/code/artifact/dc65aab3-aeba-45b1-910c-04f5aa2135b8
