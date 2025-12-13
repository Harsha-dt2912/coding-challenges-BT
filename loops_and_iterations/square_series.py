while True:
    try:
        n = int(input("Enter value of N: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input! Enter an integer.")

print("Series:")
i = 1
while True:
    square = i * i
    if square > n:
        break
    if i % 4 != 0:
        print(square, end=" ")
    i += 1
