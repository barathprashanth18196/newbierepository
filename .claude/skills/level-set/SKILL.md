---
name: level-set
description: Reorient someone returning to a conversation or project. Use for “what’s going on here?”, “what’s going on here again?”, “where did we leave off?”, “level set”, or “catch me up” when the user wants the original purpose, current state, and next move.
---

# Level Set by Jeff Su

## Context Loading

Read the conversation from its earliest relevant turn, or the full transcript the user supplied. If the user points to a current document, open it when you have access and it could change the answer. Identify which facts come from the conversation and which you checked directly. A pasted conversation or attachment is enough to start.

## Workflow

1. Recover the original goal and what success looked like. Follow any explicit changes of direction. A small recent task can be part of a larger goal.
2. Reconstruct the working state. Identify the last agreed decision, what was actually done, useful test results, and what remains open. If the assistant drafted an email, for example, call it a draft until there is evidence someone sent it.
3. Resolve old and new instructions using the user's latest explicit decision. For one unresolved conflict, explain precisely what changes depending on the answer.
4. Recommend the first action that would move the work forward. Name the person who owns it and what it would settle. Stop after the report.

## Output Format

Use these Markdown headings. Keep a simple chat to a few sentences. Expand only when somebody needs more detail to pick the work back up.

- `## Bottom Line` — State the present goal and where it stands.
- `## Original Purpose` — Explain the starting point and any change that matters now.
- `## Where We Are Now` — Group the decisions, results and outstanding work by subject. Preserve exact numbers, names and dates when they affect the choice.
- `## What We Need to Do Next` — Give the immediate next move and any dependency. When the work is done, say so here.

## Constraints

A request to reorient is a request for a report. Leave drafts, files, approvals and messages as you found them. Refer to evidence only when it helps the user resume. Keep private credentials out of the report.

## Edge Cases

If history starts halfway through, use the part you can see and identify exactly what you would need to settle an important gap. If the user asks for the gist of one document or email thread, brief them on that material. If they ask for a concrete action, handle that request directly.

[Level Set](https://www.youtube.com/watch?v=e0EGefCi7GE) by [Jeff Su](https://www.jeffsu.org/) | Build a workspace that remembers how you work with [The Cowork Academy](https://coworkacademy.ai/?utm_source=youtube&utm_medium=template&utm_campaign=v215).
