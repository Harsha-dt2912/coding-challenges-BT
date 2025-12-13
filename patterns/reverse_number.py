while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input! Enter an integer.")

original = num
reverse = 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Original Number:", original)
print("Reversed Number:", reverse)
