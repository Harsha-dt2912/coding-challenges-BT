while True:
    try:
        n = int(input("Enter number of terms: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input! Enter an integer.")

print("Series:")
value = 1
sign = 1

for _ in range(n):
    print(sign * value, end=" ")
    value += 4
    sign *= -1
