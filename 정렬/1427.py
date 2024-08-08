N = list(map(int, input()))

N.sort(reverse=True)

result = ''

for i in range(len(N)):
    result += str(N[i])

print(result)