N, M = map(int, input().split())
arr = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j + 1):
        arr[n - 1] = k

for i in range(N):
    print(arr[i], end=' ')