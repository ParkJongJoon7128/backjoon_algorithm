M = int(input())
N = int(input())

arr = []

for i in range(M, N + 1):
    if(i > 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            arr.append(i)

if(len(arr) < 1):
    print(-1)
else:
    print(sum(arr))
    print(min(arr))