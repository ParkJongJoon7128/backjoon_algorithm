a = int(input())
b = int(input())

first_result = a * (b % 10)
second_result = a * (b % 100 // 10)
third_result = a * (b // 100)

print(first_result)
print(second_result)
print(third_result)
print(a * b)