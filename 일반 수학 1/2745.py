N, B = input().split()
str_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

N = N[::-1]

for i in range(len(N)):
    result += (int(B) ** i) * str_list.index(N[i])

print(result)