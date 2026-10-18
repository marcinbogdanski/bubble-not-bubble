# Claude cross-check brief (second-vendor check of a Codex-written note)

Today's date is given in your task. Working directory: /Users/user/Projects/bubble-not-bubble.
You are an independent cross-checker with fresh context for an evidence-backed
report on whether AI investment is a bubble. Do not spawn subagents. Use
WebSearch and WebFetch with at most 15 fetches, primary sources first; for SEC
fetches use a generic User-Agent such as 'research-bot contact@example.com',
never a personal email. Read report/methodology.md and tasks/RESEARCH_BRIEF.md,
then the note named in your task, which was written by a Codex (OpenAI) agent
and corrected once after a Codex cross-check (its review is in reviews/ with
the suffix -codex-xcheck.md; read it too). You are the first Claude reviewer:
look for what a same-vendor reviewer may have accepted too easily, in either
direction, and for shared blind spots.

Do this: (1) re-verify the 12 most load-bearing claim rows; record figure,
match, grade. (2) Check the arithmetic of every derived figure in Analysis.
(3) Omissions that change the conclusions, especially from the last 30 days
and from primary filings the note did not open. (4) Assess each Summary
bullet: supported by the note's own evidence, and concrete (figure and date)?
(5) Your own one-paragraph assessment: comfortably profitable or overextended,
who loses first, and where you differ from the note. (6) Say which figures on
report/index.md or report/stack.md come from this note and whether they still
hold.

Write reviews/<note-name>-claude-xcheck.md with sections: Verdict (3 lines),
Claim re-verification (table: claim #, note's value, your value, source,
match?, grade), Arithmetic checks, Omissions, Summary-bullet assessment, Your
assessment, Front-page figures (table), Recommended edits (numbered, concrete,
with replacement text). Do not edit the note or any other file. Do not run
git. Finish by reporting the Verdict, the front-page figures that no longer
hold, and the recommended edits.
