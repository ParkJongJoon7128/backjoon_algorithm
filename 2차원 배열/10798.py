arr = [[] for _ in range(15)]
result = ''

for _ in range(5):
    str = list(input())
    for i in range(len(str)):
        arr[i].append(str[i])


for i in range(len(arr)):
    result += ''.join(arr[i])

print(result)
