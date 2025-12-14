n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

total = sum(arr)

print("Array elements:", arr)
print("Sum of array elements:", total)
