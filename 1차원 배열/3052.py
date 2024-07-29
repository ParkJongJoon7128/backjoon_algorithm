arr = []

for _ in range(10):
    n = int(input())
    arr.append(n % 42)

result = set(arr)

print(len(result))