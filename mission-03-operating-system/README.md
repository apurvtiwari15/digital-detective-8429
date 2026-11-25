# Mission 3 — Understand the Operating System

## 1. Task / objective
Explore the operating system environment, running processes, storage usage, absolute vs. relative paths, and file permissions, and explain the core responsibilities of an operating system in my own words.

## 2. Work completed
- Inspected the OS version, processor architecture, active user identity (redacted), root disk space, and running processes in Terminal.
- Examined process IDs (PIDs) and examples of system/background processes.
- Compared absolute and relative paths using the assignment repository and its subfolder.
- Inspected file permissions on `terminal-practice/notes.txt` without modifying any system permissions.
- Completed the OS responsibilities table with explanations and examples.

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| --- | --- | --- |
| Operating system / system details | Shows the OS name, version, build, and CPU architecture. | `macOS 27.2.1` (Build `26B131`), `arm64` architecture. |
| Current account identity | Identifies which user account owns the current Terminal session. | `[redacted]` (standard non-root user account). |
| Available and used storage | Reports total capacity, used space, and free space on the mounted disk. | Root filesystem `/` has `228Gi` total size, `13Gi` used, and `89Gi` available. |
| System activity snapshot | Displays currently running processes and their unique process IDs (PIDs). | Observed `launchd` (PID `1`), `logd` (PID `539`), `UserEventAgent` (PID `542`), and `systemstats` (PID `549`). |

### Task 3.2 — Understand processes
- **What is a process?** A process is an active, running instance of a program in memory, managed by the operating system.
- **What does the PID column represent?** PID stands for Process Identifier—a unique number assigned by the OS to each running process so the system can track, schedule, and manage it.
- **Two examples of processes running on my computer:** `/sbin/launchd` (PID `1`, the system service manager) and `/usr/libexec/logd` (PID `539`, the background logging daemon), alongside user applications such as a web browser or text editor.

### Task 3.3 — Understand paths and permissions
- **Absolute path vs. relative path:** An absolute path starts from the root directory `/` and specifies the complete location regardless of where you currently are (for example, `/Users/[redacted]/Desktop/digital-detective-8429/terminal-practice/notes.txt`). A relative path is resolved starting from your current working directory (for example, `terminal-practice/notes.txt` when inside `digital-detective-8429`, or `..` to go up one folder).
- **Owner permissions observed:** Running `ls -l terminal-practice/notes.txt` showed `-rw-r--r--@`. The first character `-` means it is a regular file, and the next three characters `rw-` are the owner's permissions:
  - `r` (Read): Yes, the owner can read/open the file.
  - `w` (Write): Yes, the owner can edit/modify the file.
  - `x` (Execute): No (`-`), the file is not marked as an executable program.

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| --- | --- | --- |
| Process management | Starts, schedules, pauses, and terminates running programs so multiple tasks can share the CPU fairly. | Switching smoothly between a web browser, Terminal, and a code editor. |
| Memory management | Allocates RAM to active programs, keeps each program's memory isolated, and frees memory when programs close. | Giving RAM to Python when running a script and reclaiming it after it exits. |
| Device management | Communicates with hardware devices through drivers and coordinates access to them. | Sending keystrokes from the keyboard to the active window or printing to a printer. |
| File management | Organises data into files and directories on storage drives and tracks where data is stored. | Creating `terminal-practice/notes.txt` and reading it back later. |
| User interface / shell | Provides a way for users to interact with the system, either graphically or via typed commands. | Using macOS Finder (GUI) or `zsh` in Terminal (CLI). |
| Security and permissions | Controls who can access files, run programs, or change system settings to protect data. | Allowing the file owner to write (`rw-`) while restricting other users to read-only (`r--`). |

## 3. Commands / tools used
- `sw_vers`: Displays the macOS product name, version, and build number.
- `uname -m`: Shows the machine hardware architecture (`arm64`).
- `whoami`: Prints the active user account name (redacted in documentation).
- `df -h /`: Reports disk space usage and available storage in human-readable units.
- `ps -eo pid,comm`: Lists running processes with their PID and command path.
- `ls -l`: Shows file permissions, owner, size, and timestamps.

## 4. My understanding
The operating system acts as the coordinator between hardware and user applications. It assigns each running program a process ID, manages memory and disk space safely, enforces file permissions so users and apps do not overwrite restricted data, and exposes paths and shells so we can navigate and control the machine reliably.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [README.md](README.md)
- [../evidence/mission-03-os.txt](../evidence/mission-03-os.txt)

## 8. Commit details
- Commit message: `Document operating system and file management`
- Pushed to `origin/main` on GitHub and verified.
