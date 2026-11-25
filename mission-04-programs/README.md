# Mission 4 — How Programs Run

## 1. Task / objective
Write and run a simple Python program (`hello.py`) from the Terminal and compare how compilers and interpreters translate or execute source code.

## 2. Work completed
- Created `mission-04-programs/hello.py` containing `print("Hello from Python")`.
- Executed `python3 mission-04-programs/hello.py` in Terminal and confirmed `Hello from Python` appeared as output.
- Completed the compiler vs. interpreter comparison table and written explanation.

### Task 4.1 — Create and run a Python program
- File created: `mission-04-programs/hello.py`
- Command run: `python3 mission-04-programs/hello.py`
- Observed output: `Hello from Python`

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| --- | --- | --- |
| When translation / execution happens | Translates the entire source code into machine code before the program runs. | Reads, translates, and executes instructions line by line (or via bytecode) at runtime. |
| Typical output | A standalone executable binary or object file saved to disk. | Immediate program output directly from running the source code, without a separate native binary. |
| One example | C (`gcc` / `clang`) or Rust (`rustc`). | Python (`python3`) or Ruby. |
| One advantage | Compiled programs usually run faster because translation is already done ahead of time. | Faster edit-test cycle and easier cross-platform execution without a separate build step. |

**Explanation in my own words:** As shown in the comparison table, the main difference between a compiler and an interpreter is when translation happens. A compiler translates the whole program ahead of time and produces an executable file, which makes the finished program fast to run later. An interpreter, like `python3` when running `hello.py`, translates and carries out the instructions at runtime, so there is no separate executable file to build before testing. Some modern runtimes combine both ideas—for example, Python compiles source code to bytecode first and then interprets that bytecode.

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py`: Executed the Python script using the Python 3 interpreter.
- `git add`, `git commit`, `git push`: Recorded and published Mission 4 to GitHub.

## 4. My understanding
Computers cannot directly understand human-readable source code, so a translator is always needed. Whether a language uses ahead-of-time compilation or runtime interpretation shapes how fast the code executes and how quickly a programmer can test changes.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [hello.py](hello.py)
- [README.md](README.md)

## 8. Commit details
- Commit message: `Compare compilers and interpreters`
- Pushed to `origin/main` on GitHub and verified.
