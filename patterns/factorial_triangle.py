while True:
    try:
        n = int(input("Enter number of rows: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input! Enter an integer.")

num = 1
fact = 1

for i in range(1, n + 1):
    for _ in range(i):
        fact *= num
        print(fact, end=" ")
        num += 1
    print()
