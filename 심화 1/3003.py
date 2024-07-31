n = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]

result = []

for i in range(len(n)):
    result.insert(i, chess[i] - n[i])

for i in range(len(n)):
    print(result[i], end=" ")