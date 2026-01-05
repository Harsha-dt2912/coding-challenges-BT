n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

print("Original array:")
print(arr)

arr.reverse()

print("Reversed array:")
print(arr)
