N = int(input())

result = N

for i in range(N):
    str = input()
    for j in range(0, len(str) - 1):
        if(str[j] == str[j + 1]):
            pass
        elif(str[j] in str[(j + 1) ::]):
            result -= 1
            break

print(result)
