# Times New Roman

A SwiftUI trivia game about the Times New Roman typeface and the history of
typography, with an iOS 26 "Liquid Glass" UI (and a graceful fallback for
iOS 17–25).

## Layout

Everything lives at the repo root (flat, no subfolders) except the one place
GitHub *requires* a subfolder — `.github/workflows/`:

- `*.swift` — the SwiftUI app
  - `GlassCard.swift` — reusable Liquid Glass container/button style, with an
    `.ultraThinMaterial` fallback on iOS < 26
  - `Models.swift` — `Question` model + `QuizViewModel`
  - `StartView.swift`, `QuizView.swift`, `ResultView.swift` — the three screens
- `questions.json` — 500 quiz questions
- `generate_questions.py` — the script that generated `questions.json`
- `project.yml` — [XcodeGen](https://github.com/yonaskolb/XcodeGen) spec; CI
  generates the actual `.xcodeproj` from this file rather than committing a
  hand-edited project file. It pulls all `*.swift` files from the repo root
  and bundles `questions.json` as a resource.
- `.github/workflows/build.yml` — CI that builds the app for the iOS
  Simulator on every push/PR

## About the 500 questions

Real, fact-checkable trivia about a single typeface tops out well under 500
unique items. Rather than pad the set with invented "facts," the question
bank was broadened to cover:

- **Times New Roman specifically** (~20 hand-written questions: Morison,
  Lardent, The Times, Monotype, etc.)
- **Printing/type history** (Gutenberg, Linotype, Monotype, letterpress, font
  formats)
- **Other well-known typefaces** (designer, release year, foundry,
  serif/sans-serif classification) — generated from a hand-verified table of
  ~30 real typefaces, so every fact is checkable
- **Typography terminology** (kerning, x-height, ligature, etc.)

Every question is generated from a small, curated, fact-checked data table in
`generate_questions.py` rather than written one-by-one from memory, so you can
audit or extend the source facts directly instead of trusting 500 free-form
claims. Re-run `python3 generate_questions.py` any time to regenerate
`questions.json` (e.g. after editing the fact tables).

## Running locally

You'll need Xcode 26+ (for the real Liquid Glass APIs) and
[XcodeGen](https://github.com/yonaskolb/XcodeGen) (`brew install xcodegen`).

```bash
xcodegen generate
open TimesNewRoman.xcodeproj
```

Then run on an iOS 26 simulator to see full Liquid Glass, or an iOS 17+
simulator to see the fallback styling.

## Uploading to GitHub

Browser file-picker uploads often flatten or drop folder structure, which is
why this repo avoids subfolders. If you're uploading via the GitHub web UI:

1. Drag all the `.swift` files, `questions.json`, `generate_questions.py`,
   `project.yml`, and `README.md` into the upload box at once (multi-select,
   not one at a time).
2. For `.github/workflows/build.yml`, GitHub's web UI lets you type a path
   with slashes directly into the "Create new file" name field — type
   `.github/workflows/build.yml` and it will create the folders for you.
3. Or, better: install git and push from the command line, which preserves
   folder structure automatically —
   `git init && git add . && git commit -m "init" && git branch -M main && git remote add origin <your-repo-url> && git push -u origin main`.

## CI

`.github/workflows/build.yml` runs on `macos-26` GitHub-hosted runners,
regenerates the Xcode project with XcodeGen, and does an unsigned build for
the iOS Simulator — no Apple Developer account or signing certificate needed.
If the runner's default Xcode version ever moves past 26.6, update the
`xcode-select` line in the workflow to match (check the "Select Xcode 26"
step's error message, or `ls /Applications | grep Xcode` in a workflow run,
to see what's actually installed).
