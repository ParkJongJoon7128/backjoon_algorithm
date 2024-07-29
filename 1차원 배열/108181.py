N = int(input())
arr = list(map(int, input().split()))

max = arr[0]
min = arr[0]

for i in range(N):
    if(max > arr[i]):
        max = arr[i]

for i in range(N):
    if(min < arr[i]):
        min = arr[i]

print(max, min, end=' ')