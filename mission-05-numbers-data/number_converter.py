"""Convert a user-entered decimal integer into binary and hexadecimal."""


def main() -> None:
    raw = input("Enter a non-negative decimal integer: ").strip()
    try:
        number = int(raw)
    except ValueError:
        print("Invalid input: please enter a whole decimal number.")
        return

    if number < 0:
        print("Please enter a non-negative integer (0 or greater).")
        return

    binary_value = bin(number)
    hex_value = hex(number)

    print(f"Decimal: {number}")
    print(f"Binary: {binary_value} (without prefix: {binary_value[2:]})")
    print(f"Hexadecimal: {hex_value} (without prefix: {hex_value[2:].upper()})")


if __name__ == "__main__":
    main()
