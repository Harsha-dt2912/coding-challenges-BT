n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

# Binary search requires sorted array
arr.sort()

key = int(input("Enter element to search: "))

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at position:", mid)
        found = True
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if not found:
    print("Element not found")
