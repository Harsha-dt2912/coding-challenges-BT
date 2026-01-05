n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

# minimum = arr[0]

# for i in range(1, n):
#     if arr[i] < minimum:
#         minimum = arr[i]
minimum = min(arr)

print("Minimum value in the array is:", minimum)
