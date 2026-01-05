n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

# maximum = arr[0]

# for i in range(1, n):
#     if arr[i] > maximum:
#         maximum = arr[i]
maximum = max(arr)

print("Minimum value in the array is:", maximum)
