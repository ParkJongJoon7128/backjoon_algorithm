N, M = map(int, input().split())
arr = [0] * N

for i in range(N):
    arr[i] = i + 1

for _ in range(M):
    i, j = map(int, input().split())
    arr[i - 1], arr[j - 1] = arr[j - 1], arr[i - 1]

for n in range(N):
    print(arr[n], end=' ')