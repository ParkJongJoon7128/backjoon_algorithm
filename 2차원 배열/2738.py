N, M = map(int, input().split())

A, B = [], []

for _ in range(N):
    row_A = list(map(int, input().split()))
    A.append(row_A)

for _ in range(N):
    row_B = list(map(int, input().split()))
    B.append(row_B)

for i in range(N):
    for j in range(M):
        result = A[i][j] + B[i][j]
        print(result, end=' ')
    print()