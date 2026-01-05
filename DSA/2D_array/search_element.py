rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Enter element [{i}][{j}]: ")))
    matrix.append(row)

key = int(input("Enter element to search: "))

found = False

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == key:
            found = True
            break
    if found:
        break

if found:
    print("Element found in the 2D array")
else:
    print("Element not found in the 2D array")
