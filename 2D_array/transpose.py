# Read matrix dimensions
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

# Create matrix
matrix = []

print("Enter matrix elements:")
for i in range(m):
    row = []
    for j in range(n):
        value = int(input(f"Element [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

# Display original matrix
print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Display transpose
print("\nTranspose of Matrix:")
for j in range(n):
    for i in range(m):
        print(matrix[i][j], end=" ")
    print()
