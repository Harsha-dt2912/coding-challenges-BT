n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

key = int(input("Enter element to search: "))

found = False
for i in range(n):
    if arr[i] == key:
        print(f"Element {key} found at position {i + 1}")
        found = True
        break

if not found:
    print(f"Element {key} not found at the array")
