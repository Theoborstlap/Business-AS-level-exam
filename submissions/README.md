# Submit your answers & get them marked

This folder is a self-marking system. Add a file with your answers, commit it,
and a GitHub Action automatically marks it and commits a feedback report back
into this folder. You can submit **as many times as you like**.

## How to submit (all in the GitHub website - no software needed)

1. Open this `submissions/` folder on GitHub and click **Add file -> Create new file**.
2. Name your file something like `my-answers-B1.md` (it **must end in `.md`** and
   **must not** end in `.feedback.md`).
3. Paste the template below, set the `set:` and `paper:` header, and type your answers.
4. Scroll down and click **Commit changes** (commit to the branch these files live on).
5. Wait ~1 minute. Refresh the folder: a new file `my-answers-B1.feedback.md`
   appears with your marks and feedback. Open it to read it.
6. To try again, just **edit** your answer file and commit again - the feedback
   is regenerated. (Or create a new file for a different paper.)

You can also watch progress under the repository's **Actions** tab.

## File format

```
set: B          # A = the exam papers (Set A), B = the knowledge check (Set B)
paper: B1       # Set A uses 1-16, Set B uses B1-B10
name: Theo      # optional

## Q1
(a) your answer to part (a) ...
(b) your answer to part (b) ...
(c) your answer to part (c) ...

## Q2
your answer here (for a question that has no (a)/(b) parts)

## Q5
(a) ...
(b) ...
```

Rules that make marking reliable:
- Start each question with a line like `## Q1`, `## Q2`, ... (the number must
  match the question number in the paper/PDF).
- If a question has parts, start each part with `(a)`, `(b)`, `(c)` ...
- Answer as many or as few questions as you want - only what you submit is marked.

## How marking works

- **Knowledge / short-answer** questions are marked by matching the key points
  in your answer against the mark scheme (about one mark per correct point).
- **Calculation** questions are marked by checking your final numerical answer.
- **Essay / "evaluate"** questions get an **indicative** level and mark, plus a
  checklist (knowledge, both sides, application, judgement) and the full level
  descriptors so you can self-assess.

Knowledge and calculation marks are reliable. Essay marks are an automated
estimate to guide revision - they are **not** a substitute for a teacher's mark.
Every question's model answer / mark scheme is included in the feedback so you
can always check for yourself.

See `TEMPLATE.md` for a blank starting point and `example-setB-B1.md` for a
worked example (its feedback is `example-setB-B1.feedback.md`).
