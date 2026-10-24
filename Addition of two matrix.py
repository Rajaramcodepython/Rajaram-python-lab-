# Addition of two matrices

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [1, 2, 3]]

C = [[0, 0, 0],
     [0, 0, 0]]

for i in range(2):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]

print("Addition of two matrices:")
for row in C:
    print(row)
