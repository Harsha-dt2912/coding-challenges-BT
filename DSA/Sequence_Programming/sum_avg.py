def get_number(prompt):

    while True:
        value = input(prompt).strip()

        # Check for empty input
        if value == "":
            print("Input cannot be empty. Please enter a valid number.")
            continue

        # Validate numeric input (supports integer & float)
        try:
            number = float(value)
            return number
        except ValueError:
            print("Invalid input! Please enter a valid numeric value.")


def main():
    print("=== Sum and Average Calculator ===")

    # Get validated input
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    # Calculate sum and average
    sum = num1 + num2
    average = sum / 2

    #output
    print("\nResults:")
    print(f"Sum = {sum}")
    print(f"Average = {average}")


if __name__ == "__main__":
    main()
