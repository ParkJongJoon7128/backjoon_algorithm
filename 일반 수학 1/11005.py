N, B = map(int, input().split())
str_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''

while N:
    result += str_list[N % B]
    N //= B

print(result[::-1])
