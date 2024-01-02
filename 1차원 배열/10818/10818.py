N = int(input())
list = list(map(int, input().split()))
max = list[0]
min = list[0]

for i in range(N):
    if (max < list[i]):
        max = list[i]
    if (min > list[i]):
        min = list[i]

print("%d %d" %(min, max))