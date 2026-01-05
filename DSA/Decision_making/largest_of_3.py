def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

a = get_number("Enter first number: ")
b = get_number("Enter second number: ")
c = get_number("Enter third number: ")

largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c

print("The largest number is:", largest)
