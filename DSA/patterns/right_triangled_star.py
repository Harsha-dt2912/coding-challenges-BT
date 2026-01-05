while True:
    try:
        n = int(input("Enter number of rows: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input! Enter an integer.")

for i in range(1, n + 1):
    print("*" * i)
