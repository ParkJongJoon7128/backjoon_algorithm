A = int(input())
B = int(input())

num1 = B % 10
num2 = (B % 100) // 10
num3 = B // 100

result1 = A * num1
result2 = A * num2
result3 = A * num3

print(result1)
print(result2)
print(result3)
print(A * B)