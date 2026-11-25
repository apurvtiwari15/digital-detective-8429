# Mission 6 — Git and GitHub

## 1. Task / objective
Understand the core Git workflow (status, staging, committing, and history), create and publish a feature branch (`update-about`), open a Pull Request on GitHub, explain why branches and Pull Requests are useful, and build a personal Git command glossary.

## 2. Work completed
- Inspected repository status and recent commit history on `main`.
- Created the `update-about` branch, added a `My Learning` section to the root `README.md`, staged and committed the change, and pushed `update-about` to GitHub.
- Opened Pull Request #1 (`update-about` → `main`) on GitHub: `https://github.com/apurvtiwari15/digital-detective-8429/pull/1`.
  - **PR Status:** Open (not merged, kept open so the branch and Pull Request activity remain visible for instructor review).
- Switched back to `main` and documented the Git workflow and glossary below.

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| --- | --- |
| Check repository status (`git status`) | Shows the current branch, modified or untracked files, and which changes are staged for the next commit. |
| Stage selected changes (`git add <file>`) | Copies the current changes of a chosen file into the staging area (index) so they will be included in the next commit. |
| Create a commit (`git commit -m "..."`) | Saves a permanent snapshot of everything currently in the staging area to the local repository history with a descriptive message. |
| View commit history (`git log --oneline`) | Lists past commits with their short commit IDs and messages so you can trace how the project evolved. |

**Difference between staging (`git add`) and committing (`git commit`):** Staging selects and prepares specific changes in a temporary holding area before they are recorded, letting you review or group edits carefully. Committing permanently records that staged snapshot into the repository's history.

### Task 6.2 & 6.3 — Branches and Pull Requests
- **Branch created:** `update-about` (commit `2b7fa92`: `Add My Learning section to root README`).
- **Pull Request created:** `https://github.com/apurvtiwari15/digital-detective-8429/pull/1` (`update-about` into `main`).
- **PR status:** Open (unmerged, per assignment instructions to merge only if requested by the instructor).
- **What a branch is and why it is useful:** A branch is an independent line of development that lets you work on a new feature or documentation update without affecting the stable `main` branch.
- **What a Pull Request is and why it is useful:** A Pull Request (PR) is a proposal on GitHub to merge changes from one branch into another. It shows a clear diff of every line changed and gives teammates or instructors a place to review, discuss, and approve changes before they enter `main`.

### Task 6.4 — Git command glossary

| Operation | Command | One-line explanation |
| --- | --- | --- |
| Initialise a repository | `git init` | Creates a new local Git repository in the current folder. |
| Check status | `git status` | Displays the active branch and lists modified, untracked, and staged files. |
| Stage changes | `git add <path>` | Adds file changes to the staging area in preparation for the next commit. |
| Commit changes | `git commit -m "<message>"` | Records staged changes as a permanent snapshot in local Git history. |
| View history | `git log` | Shows the chronological list of commits made in the repository. |
| Create or list branches | `git branch [name]` | Lists existing local branches, or creates a new branch when a name is given. |
| Switch branches | `git checkout <branch>` (or `git switch <branch>`) | Moves the working directory to the specified branch. |
| Publish changes | `git push [remote] [branch]` | Uploads local commits on a branch to a remote repository like GitHub. |
| Retrieve remote changes | `git pull` | Fetches new commits from the remote repository and merges them into the current branch. |

## 3. Commands / tools used
- `git status`, `git add`, `git commit`, `git log --oneline`: Practised inspecting, staging, committing, and reviewing history.
- `git checkout -b update-about`, `git push -u origin update-about`, `git checkout main`: Created, published, and switched between branches.
- `gh pr create`: Opened Pull Request #1 from `update-about` into `main` on GitHub.

## 4. My understanding
Git separates editing, staging, and committing so you can craft clean, focused commits. Branches isolate in-progress work from `main`, and Pull Requests make collaboration safe by letting others review changes before merging.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [README.md](README.md)
- Branch `update-about` on GitHub
- Pull Request #1: https://github.com/apurvtiwari15/digital-detective-8429/pull/1

## 8. Commit details
- Commit message: `Complete Git and GitHub collaboration mission`
- Pushed to `origin/main` on GitHub and verified.
