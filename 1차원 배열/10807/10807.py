N = int(input())
list = list(map(int, input().split()))
v = int(input())
sum = 0

for i in range(N):
    if(list[i] == v):
        sum += 1

print(sum)