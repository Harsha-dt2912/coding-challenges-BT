n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

even_count = 0
odd_count = 0

for num in arr:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
print("Array elements:", arr)
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
