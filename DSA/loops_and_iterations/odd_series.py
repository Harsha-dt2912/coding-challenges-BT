while True:
    try:
        n = int(input("Enter value of N: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input! Enter an integer.")

print("Odd number series:")
for i in range(1, n + 1, 2):
    print(i, end=" ")
