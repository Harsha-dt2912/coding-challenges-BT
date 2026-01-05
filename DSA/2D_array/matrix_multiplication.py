# Read matrix dimensions
row1 = int(input("Enter number of rows of Matrix A: "))
col1 = int(input("Enter number of columns of Matrix A: "))

row2 = int(input("Enter number of rows of Matrix B: "))
col2 = int(input("Enter number of columns of Matrix B: "))

# Check compatibility
if col1 != row2:
    print("Matrix multiplication not possible")
else:
    # Read Matrix A
    print("Enter elements of Matrix A:")
    A = []
    for i in range(row1):
        row = []
        for j in range(col1):
            row.append(int(input()))
        A.append(row)

    # Read Matrix B
    print("Enter elements of Matrix B:")
    B = []
    for i in range(row2):
        row = []
        for j in range(col2):
            row.append(int(input()))
        B.append(row)

    # Initialize result matrix with zeros
    result = [[0 for _ in range(col2)] for _ in range(row1)]

    # Matrix multiplication
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j] += A[i][k] * B[k][j]

    # Display result
    print("Resultant Matrix:")
    for row in result:
        print(row)
