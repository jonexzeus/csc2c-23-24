from itertools import permutations

def generate_codes():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    codes = list(permutations(digits, 4))
    return codes

def main():
    PIN = input("Enter a four-digit PIN code: ")

    if len(PIN) != 4 or not PIN.isdigit():
        print("Invalid input. Please enter a four-digit PIN code.")
        return

    CODES = generate_codes()

    for code in CODES:
        if PIN == ''.join(map(str, code)):
            print("OPEN")
            return

    print("PIN does not match any of the combinations. Access denied.")

if __name__ == "__main__":
    main()
