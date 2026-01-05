n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

choice = input("Enter order (asc/desc): ").lower()

if choice == "asc":
    arr.sort()
    print("Array sorted in ascending order:")
elif choice == "desc":
    arr.sort(reverse=True)
    print("Array sorted in descending order:")
else:
    print("Invalid choice")

print(arr)
