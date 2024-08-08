N = int(input())
arr = []

for _ in range(N):
    age, name = list(map(str, input().split()))
    arr.append((age, name))

arr.sort(key=lambda x: int(x[0]))

for age, name in arr:
    print(age, name)