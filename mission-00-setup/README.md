# Mission 0 — Repository and Workspace Setup

## 1. Task / objective
Create a correctly named public GitHub repository (`digital-detective-8429`), verify that Python 3 and Git are installed, set up the local mission folder structure, prepare the root `README.md`, and push the initial setup commit before starting Mission 1.

## 2. Work completed
- Verified local `python3` and `git` installations in Terminal.
- Created the required mission folders (`mission-00-setup` through `mission-08-final-report`) and `evidence/`.
- Created the initial `README.md` files in each mission folder and `mission-05-numbers-data/number_converter.py` placeholder.
- Prepared the root `README.md` with the project title, assignment overview, mission index links, and a note that each mission is committed separately.
- Connected the local repository to the public GitHub repository `digital-detective-8429`.

## 3. Commands / tools used
- `python3 --version`: Checked the installed Python version (`Python 3.13.9`).
- `git --version`: Checked the installed Git version (`git version 2.56.0`).
- `git status`: Inspected the working tree state and remote tracking.
- `git remote -v`: Verified the remote repository URL (`origin`).
- `git config user.name` / `git config user.email`: Configured local Git author identity using a privacy-safe GitHub noreply email.
- `git add`, `git commit`, `git push`: Staged, committed, and published the initial setup to GitHub.

## 4. My understanding
A Git repository is a project workspace tracked by version control so every change can be recorded as a history of commits. Organising the repository by mission keeps each topic isolated, makes progress easy to verify, and ensures that every stage of the assignment has its own clear documentation and commit history.

## 5. Difficulties faced
Local Git author identity (`user.name` and `user.email`) was not configured yet, which would prevent creating commits.

## 6. How I resolved them
Set `user.name` to `apurvtiwari15` and `user.email` to the GitHub noreply address (`apurvtiwari15@users.noreply.github.com`) in local Git config so commits work without exposing a personal email address.

## 7. Evidence / files
- [../README.md](../README.md)
- [README.md](README.md)
- Initialised folders: `mission-00-setup/` through `mission-08-final-report/` and `evidence/`

## 8. Commit details
- Commit message: `Set up Digital Detective mission structure`
- Pushed to `origin/main` on GitHub and verified.
