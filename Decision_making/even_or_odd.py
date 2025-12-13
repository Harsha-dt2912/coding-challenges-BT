def is_even_or_odd():
    # Get user input
    num_input = input("Enter a number: ")

    # Validate input
    try:
        num = int(num_input)   # Convert to integer
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    # Check even or odd
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# Run the function
is_even_or_odd()
