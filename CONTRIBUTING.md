# Contributing to cs50/problems

Thank you for your interest in helping improve CS50's problem sets and checks! Please read this document in its entirety before contributing.

> **Note:** This repository and all other CS50 repositories **are not** the place to submit your completed problem sets or to request help with assignments. If you're stuck on a problem set, please consult one of our [many communities](https://cs50.harvard.edu/x/communities/).

---

## What lives here

This repository contains the `check50` checks, `submit50` configuration, and problem specifications for CS50's online courses. There is no single `main` branch: each course offering has its own branch, named `<year>/<course>`, and most branches stop changing once that offering ends. Pull requests should target the **current** branch for the course:

| Course | Current branch |
|--------|----------------|
| CS50x | `2026/x` |
| CS50's Introduction to Programming with Python (CS50P) | `2022/python` |
| CS50's Introduction to Databases with SQL | `2024/sql` |
| CS50's Introduction to Programming with R | `2025/r` |
| CS50's Introduction to Programming with Scratch | `2024/scratch` |

Branches named `<year>/fall`, `<year>/spring`, and `<year>/summer` belong to on-campus offerings and are not open to outside contribution.

The `check50` or `submit50` slug for a problem tells you exactly where it lives. For example, in

```
check50 cs50/problems/2026/x/mario/less
```

`2026/x` is the branch and `mario/less` is the folder within it. **Whenever you open an issue or pull request, start from the slug.** It is the fastest way for staff to identify the right branch.

Bugs in the `check50` or `submit50` tools themselves (as opposed to a particular problem's checks) belong in [cs50/check50](https://github.com/cs50/check50) or [cs50/submit50](https://github.com/cs50/submit50) respectively. The projects for CS50's Introduction to Artificial Intelligence with Python (CS50 AI) live in [ai50/projects](https://github.com/ai50/projects), not here.

---

## How to contribute

CS50 uses GitHub to host code, track issues, discuss feature requests, and accept pull requests. **Please do not email staff members to propose changes.**

1. **Open an issue** to report a bug or suggest an improvement (see below). You do not need to fork anything to do this.
2. Optionally, once the issue has been discussed, **open a pull request** with your proposed change (see below).

---

## Opening an issue

Click **New issue** and choose **Bug report** or **Feature request**. GitHub will present a form; please complete every field. The first fields ask which **course** you are taking and for the problem's **slug**, so that staff can tell which branch your report concerns even if you are unsure yourself.

When describing a bug, include the exact command you ran and its full output, as long as doing so does not violate CS50's [Academic Honesty policy](https://cs50.harvard.edu/x/honesty/).

---

## Opening a pull request

1. **Find the right branch.** Take the branch name from the problem's slug (e.g. `2026/x` from `cs50/problems/2026/x/mario/less`) and confirm it is the current branch for that course in the table above. Changes are normally accepted only on current branches; branches for past offerings are kept stable so that students' results remain reproducible. If you believe a past branch needs a fix, open an issue first.
2. **Fork** this repository and create your branch **from that course branch**, not from the default branch, unless the default branch is the one you are changing.
3. Make your change. Keep it focused on a single problem or issue.
4. **Open the pull request against the same course branch** you started from. GitHub pre-selects the default branch as the base, so double-check the **base** dropdown before you submit.
5. In the description, link the issue your pull request addresses (`Fixes #123`) and state the slug(s) affected. If the same fix applies to another course's branch as well, say so; staff will cherry-pick rather than asking you to open several pull requests.

A member of the CS50 staff will review your issue or pull request and follow up as needed. If a pull request was opened against the wrong branch, staff will usually retarget it, but telling us the slug up front saves everyone time.
