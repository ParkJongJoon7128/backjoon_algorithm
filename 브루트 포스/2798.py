N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            current_value = arr[i] + arr[j] + arr[k]
            if((current_value <= M) and (current_value > result)):
                result = current_value

print(result)