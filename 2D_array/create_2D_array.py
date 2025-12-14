rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    print(f"Enter elements for row {i + 1}:")
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

print("\n2D Array (Row-wise):")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
