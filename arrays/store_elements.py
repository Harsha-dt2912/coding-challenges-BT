n = int(input("Enter size of array: "))
arr = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

print("Array elements are:")
print(arr)
