A = [
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [3, 6, 9, 12]
]
print("Matrix A:")
for i in range(3):
    for j in range(4):
        print(A[i][j], end=" ")
    print()
B = []
for i in range(3):
    row = [0] * 4 
    B.append(row)
print("\nMatrix B:")
for i in range(3):
    for j in range(4):
        print(B[i][j], end=" ")
    print()
C = []
for i in range(3):
    C.append([0] * 4)
print("\nMatrix C:")
for i in range(3):
    for j in range(4):
        print(C[i][j], end=" ")
    print()
    print("this is the desire output for the given. matrix")