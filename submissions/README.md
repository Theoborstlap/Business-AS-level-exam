# Submit your answers & get them marked

This folder is a self-marking system. Add a file with your answers, commit it,
and a GitHub Action marks it and commits a feedback report back here. You can
submit **as many times as you like**, answer **any subset** of questions, cover
**several papers in one file**, and even submit **handwritten answers as photos**.

## Easiest: the submission box (open an Issue)

The simplest "drop box" is a GitHub **Issue**:

1. Go to the repo's **Issues** tab -> **New issue** -> **Submit answers for marking**.
2. In the box, set `paper:` and type your answers under `## Q1`, `## Q2` ...
   **To submit handwriting, just drag a photo into the box** - it uploads and
   inserts an image link; put it under the right `## Q` heading.
3. Click **Submit new issue**. Within a couple of minutes the marker **replies
   with your marks and feedback as a comment**. Edit the issue to be re-marked.

This needs no files and works on mobile. The file method below still works too.

## How to submit (all in the GitHub website - no software needed)

1. Open this `submissions/` folder on GitHub -> **Add file -> Create new file**
   (or **Upload files** for photos).
2. Name your file ending in **`.md`** (not `.feedback.md`), e.g. `my-answers.md`.
3. Paste the template below, set the `paper:` header and type (or photograph) your answers.
4. **Commit changes** to the branch these files live on.
5. Wait ~1 minute, refresh, and open the new `my-answers.feedback.md` for your marks.
6. Try again any time by editing the file and committing again.

You can watch each run under the repository's **Actions** tab.

## File format

```
paper: B1        # Set A uses 1-16, Set B uses B1-B10 (the "B" tells it which set)
name: Theo       # optional

## Q1
(a) your answer to part (a) ...
(b) your answer to part (b) ...

## Q5
your answer here (for a question with no (a)/(b) parts)
```

Rules that make marking reliable:
- Start each question with `## Q1`, `## Q2`, ... (number = question number in the paper/PDF).
- If a question has parts, start each part with `(a)`, `(b)`, `(c)` ...
- Answer as many or as few questions as you want - only what you submit is marked.

## Multiple papers in one file

Just repeat the `paper:` line to start a new paper. Everything after it belongs
to that paper until the next `paper:` line. Example:

```
name: Theo

paper: B1
## Q1
(a) ...
(b) ...

paper: 7            # switches to Set A, Paper 7
## Q3
...

paper: B10
## Q2
...
```

Your feedback file then has an **Overall** total plus a section per paper.
You can also just commit **several separate `.md` files** - each gets its own
feedback report.

## Handwriting / photos (OCR)

You can submit handwritten answers as images (`.jpg`, `.jpeg`, `.png`, `.webp`,
`.heic`, ...). Two ways:

**A) Reference a photo from your answer file** - upload the image into this
folder, then point to it:

```
paper: B1
## Q1
(a) img: q1a.jpg
(b) img: q1b.jpg
## Q2
img: q2.jpg
```

(`img:`, `image:`, `photo:` or a Markdown image `![](q1a.jpg)` all work. A
`.txt` reference is read directly as a typed transcription.)

**B) Just upload named photos - zero typing.** Name each image with the paper
and question and it is marked automatically, e.g.:

```
B1-Q1.jpg        ->  Set B, Paper B1, Question 1
B1-Q3a.jpg       ->  Set B, Paper B1, Question 3 part (a)
7-Q11.png        ->  Set A, Paper 7, Question 11
A2-Q1.jpg        ->  Set A, Paper 2, Question 1
```

Feedback for photo-only papers is written to `handwritten-<paper>.feedback.md`.

**Important about handwriting:** the answer is read by an OCR engine, so the
transcription is shown under *"Your answer"* in your feedback - always check it
was read correctly. For best results write neatly (block capitals are safest),
photograph straight-on in good light, and keep one question per photo. If the
writing is misread you may score lower than you deserve - typing is always the
most accurate.

## How marking works

- **Knowledge / short answers** -> key points matched against the mark scheme.
- **Calculations** -> your final numerical answer is checked.
- **Essays / "evaluate"** -> an **indicative** level & mark, a checklist
  (knowledge / two sides / application / judgement) and the full level
  descriptors so you can self-assess.

Knowledge and calculation marks are reliable. Essay marks are an automated
estimate to guide revision - not a substitute for a teacher's mark. Every
question's model answer is included so you can always check for yourself.

See `TEMPLATE.md` for a starting point and `example-setB-B1.md` /
`example-setA-P2.md` for worked examples with feedback.
