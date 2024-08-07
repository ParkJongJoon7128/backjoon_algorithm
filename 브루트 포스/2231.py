N = int(input())
result = 0

for i in range(1, N + 1):
    split_number = list(map(int, str(i)))
    result = sum(split_number) + i

    if(result == N):
        print(i)
        break
    if(i == N):
        print(0)