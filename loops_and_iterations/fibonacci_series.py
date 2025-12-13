while True:
    try:
        n = int(input("Enter value of N: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input! Enter an integer.")

print("Fibonacci Series:")
a, b = 1, 1

while a <= n:
    print(a, end=" ")
    a, b = b, a + b
