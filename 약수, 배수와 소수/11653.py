N = int(input())
result = []

i = 2

while i <= N:
    if N % i == 0:
        result.append(i)
        N //= i
    else:
        i += 1

for i in result:
    print(i, sep='\n')