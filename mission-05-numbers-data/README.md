# Mission 5 — Numbers and Data

## 1. Task / objective
Convert numbers manually between decimal, binary, and hexadecimal; verify the conversions using Python; build and test `number_converter.py`; and explain how computers represent text using character-encoding standards.

## 2. Work completed
- Solved all seven manual conversion problems in Task 5.1 with step-by-step working.
- Verified every conversion in Python 3 using `bin()`, `hex()`, and `int(..., base)`.
- Built `mission-05-numbers-data/number_converter.py` and tested it with `13`, `25`, and `255`.
- Documented ASCII codes for `A` and `a`, why encoding standards are required, and a non-ASCII character example.

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| --- | --- |
| Convert decimal 13 to binary. | `13 ÷ 2 = 6 R 1`, `6 ÷ 2 = 3 R 0`, `3 ÷ 2 = 1 R 1`, `1 ÷ 2 = 0 R 1`. Reading remainders bottom-to-top: **`1101`**. |
| Convert decimal 25 to binary. | `25 ÷ 2 = 12 R 1`, `12 ÷ 2 = 6 R 0`, `6 ÷ 2 = 3 R 0`, `3 ÷ 2 = 1 R 1`, `1 ÷ 2 = 0 R 1`. Reading remainders bottom-to-top: **`11001`**. |
| Convert binary 1010 to decimal. | `(1 × 2^3) + (0 × 2^2) + (1 × 2^1) + (0 × 2^0) = 8 + 0 + 2 + 0 =` **`10`**. |
| Convert binary 1101 to decimal. | `(1 × 2^3) + (1 × 2^2) + (0 × 2^1) + (1 × 2^0) = 8 + 4 + 0 + 1 =` **`13`**. |
| Convert hexadecimal A to decimal. | In base 16, `A` represents **`10`**. |
| Convert hexadecimal 1F to decimal. | `(1 × 16^1) + (15 × 16^0) = 16 + 15 =` **`31`**. |
| Convert binary 1111 to hexadecimal. | `1111` in binary equals `8 + 4 + 2 + 1 = 15` in decimal, which is **`F`** in hexadecimal. |

### Task 5.2 — Verify using Python

| Expression tested | Python result | Matches manual calculation? |
| --- | --- | --- |
| `bin(13)` | `'0b1101'` | Yes (`1101`) |
| `bin(25)` | `'0b11001'` | Yes (`11001`) |
| `int("1010", 2)` | `10` | Yes (`10`) |
| `int("1101", 2)` | `13` | Yes (`13`) |
| `int("A", 16)` | `10` | Yes (`10`) |
| `int("1F", 16)` | `31` | Yes (`31`) |
| `hex(int("1111", 2))` | `'0xf'` | Yes (`F`) |
| `hex(13)` | `'0xd'` | Yes (`D`, since `13` in base 16 is `D`) |
| `hex(25)` | `'0x19'` | Yes (`19`, since `1×16 + 9 = 25`) |

### Task 5.3 — Build a small number converter
`mission-05-numbers-data/number_converter.py` reads a decimal number from the user with `input()`, converts the string to an integer with `int()`, and computes its binary and hexadecimal representations using `bin()` and `hex()`.
- **`bin(number)`**: Takes an integer and returns its binary string prefixed with `0b` (base 2).
- **`hex(number)`**: Takes an integer and returns its lowercase hexadecimal string prefixed with `0x` (base 16).

| Test number | Binary output | Hexadecimal output |
| --- | --- | --- |
| `13` | `0b1101` (`1101`) | `0xd` (`D`) |
| `25` | `0b11001` (`11001`) | `0x19` (`19`) |
| `255` | `0b11111111` (`11111111`) | `0xff` (`FF`) |

### Task 5.4 — How is text stored?
- **ASCII decimal codes:** Uppercase `A` is **`65`** (`ord('A') == 65`) and lowercase `a` is **`97`** (`ord('a') == 97`).
- **Why computers need an encoding standard:** Computer memory only stores numbers made of bits (`0` and `1`), so an encoding standard is needed to map each character consistently to a specific number that every program and device can interpret the same way.
- **Character not in basic ASCII:** The Indian Rupee symbol `₹` (Unicode `U+20B9`), accented letters like `é`, or emoji like `🪔` are not part of 7-bit basic ASCII (`0–127`), and are represented using UTF-8.

## 3. Commands / tools used
- `python3`: Used to verify conversions interactively/via expressions and to run `number_converter.py`.
- Python built-in functions: `input()`, `int()`, `bin()`, `hex()`, and `ord()`.
- `git add`, `git commit`, `git push`: Recorded and published Mission 5 to GitHub.

## 4. My understanding
All data in a computer—numbers and text alike—is ultimately stored as binary bits. Hexadecimal provides a compact shorthand for binary (each hex digit maps cleanly to 4 bits), and character encodings like ASCII and UTF-8 bridge human text and binary numbers.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [number_converter.py](number_converter.py)
- [README.md](README.md)

## 8. Commit details
- Commit message: `Build number converter and practise data representation`
- Pushed to `origin/main` on GitHub and verified.
