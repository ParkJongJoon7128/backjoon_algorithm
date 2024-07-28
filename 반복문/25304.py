X = int(input())
N = int(input())
arr = []
result = 0

for i in range(N):
    a, b = map(int, input().split())
    arr.append(a * b)

for i in range(N):
    result += arr[i]

if(result == X):
    print("Yes")
else:
    print("No")
