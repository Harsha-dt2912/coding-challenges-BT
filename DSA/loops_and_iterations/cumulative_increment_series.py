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
term = 1
increment = 1

while term <= n:
    print(term, end=" ")
    term += increment
    increment += 1

#upto n terms code
# for _ in range(n):
#     print(term, end=" ")
#     term += increment
#     increment += 1