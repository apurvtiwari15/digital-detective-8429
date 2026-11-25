# Mission 2 — Become Comfortable with the Terminal

## 1. Task / objective
Use the command-line interface (CLI) to inspect folders, navigate directories, create and manage practice files safely inside `terminal-practice/`, understand command flags and pipes, and explain how package managers work.

## 2. Work completed
- Practised core Terminal file and directory commands inside the repository and `terminal-practice/`.
- Created `terminal-practice/notes.txt`, wrote a first line, appended a second line without overwriting, verified its contents, and created a renamed backup copy `terminal-practice/notes_backup.txt`.
- Compared `ls`, `ls -lah`, and `ls -l | head -n 5` to observe flags and pipes.
- Checked the installed Homebrew version (`Homebrew 7.0.8`) and counted managed formulae (`7`) without installing or uninstalling any packages.

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| --- | --- | --- |
| Current-directory display (`pwd`) | Prints the full path of the working directory. | Displayed `/Users/[redacted]/Desktop/digital-detective-8429/terminal-practice`. |
| Directory listing (`ls`) | Lists visible files and folders in the current directory. | Showed `notes.txt` and `notes_backup.txt`. |
| Detailed listing (`ls -l`) | Shows permissions, link count, owner, size, modified date, and name. | Displayed file sizes (`85` bytes) and permissions (`-rw-r--r--@`). |
| Change directory (`cd ..`) | Moves the shell session to the parent folder. | Changed location from `terminal-practice` back to `digital-detective-8429`. |
| Create directory (`mkdir -p terminal-practice`) | Creates a new folder (and parent folders if needed). | Created `terminal-practice` inside the repository. |
| Create empty file (`touch notes.txt`) | Creates an empty file or updates its timestamp if it already exists. | Created `notes.txt` inside `terminal-practice`. |
| Copy file (`cp notes.txt notes_copy.txt`) | Duplicates a file to a new path or filename. | Created `notes_copy.txt` with identical contents to `notes.txt`. |
| Move / rename file (`mv notes_copy.txt notes_backup.txt`) | Moves a file to another folder or renames it in place. | Renamed `notes_copy.txt` to `notes_backup.txt` without leaving the old name behind. |
| Display file contents (`cat notes.txt`) | Prints the contents of a file to the Terminal. | Showed both lines written to `notes.txt`. |

### Task 2.2 — Practise file changes safely
- **Difference between replacing a file's contents (`>`) and adding text to the end (`>>`):** Using `>` overwrites the entire file from the beginning, erasing any previous text, whereas `>>` appends new text to the end while keeping existing lines intact.
- **Difference between copying a file (`cp`) and moving a file (`mv`):** `cp` creates an independent duplicate so both the original and copy exist, while `mv` relocates or renames the original file so only one file remains at the new path/name.
- **Information provided by current-directory display (`pwd`):** It shows the exact absolute path from the root directory `/` down to the folder you are currently working in.
- **Why a directory-listing operation (`ls`) is useful:** It lets you quickly see what files and subdirectories exist in a location, verify filenames before running commands, and check permissions or file sizes.

### Task 2.3 — Understand flags and pipes
- **Flags (`ls` vs `ls -lah`):** Running `ls` only prints file names (`notes.txt`, `notes_backup.txt`). Adding `-l` shows long-format metadata (permissions, owner, size, timestamp), `-a` reveals hidden entries starting with `.` (such as `.` and `..`), and `-h` formats sizes in human-readable units like `85B` and `128B`.
- **Pipes (`ls -l | head -n 5`):** The pipe symbol `|` connects the standard output of the left command (`ls -l`) directly into the standard input of the right command (`head -n 5`). The left side generates the full detailed listing, and the right side filters it to display only the first 5 lines.

### Task 2.4 — Understand package managers
- **Observation:** `brew --version` reported `Homebrew 7.0.8`, and `brew list --formula | wc -l` showed `7` installed formulae.
- **Why package managers are useful:** Package managers automate downloading, installing, updating, and removing software from trusted sources instead of manually searching for installers. They also automatically resolve and install required dependencies so tools work cleanly together.

## 3. Commands / tools used
- `mkdir`, `cd`, `pwd`, `ls`, `touch`, `echo`, `cat`, `cp`, `mv`: Core shell commands for navigating folders and managing files safely.
- `head`: Displays the first few lines of input, used after a pipe (`|`).
- `brew --version`, `brew list --formula`: Checked Homebrew version and package count without modifying any installed software.

## 4. My understanding
The Terminal gives direct, repeatable control over files and directories using short text commands. Flags customize how a command behaves, pipes let small single-purpose commands work together in a chain, and package managers keep developer tools organized and up to date.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [README.md](README.md)
- [../terminal-practice/notes.txt](../terminal-practice/notes.txt)
- [../terminal-practice/notes_backup.txt](../terminal-practice/notes_backup.txt)
- [../evidence/mission-02-terminal.txt](../evidence/mission-02-terminal.txt)

## 8. Commit details
- Commit message: `Complete Terminal and file management mission`
- Pushed to `origin/main` on GitHub and verified.
