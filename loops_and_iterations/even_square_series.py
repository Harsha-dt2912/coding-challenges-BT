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
i = 2
while True:
    square = i * i
    if square > n:
        break
    print(square, end=" ")
    i += 2
#upto n terms code
# for i in range(2, n * 2+1, 2):
#     square = i * i
#     print(square, end=" ")
