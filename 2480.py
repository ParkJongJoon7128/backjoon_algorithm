a, b, c = map(int, input().split())

if(a == b == c):
    result = 10000 + a * 1000
elif(a == b or a == c):
    result = 1000 + a * 100
elif(b == a or b == c):
    result = 1000 + b * 100
elif(c == a or c == b):
    result = 1000 + c * 100
elif(a != b != c):
    result = max(a, b, c) * 100

print(result)