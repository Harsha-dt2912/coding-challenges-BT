def is_even_or_odd():
    while True:
        num_input = input("Enter a number: ").strip()
        try:
            num = int(num_input)
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

if __name__ == "__main__":
    is_even_or_odd()