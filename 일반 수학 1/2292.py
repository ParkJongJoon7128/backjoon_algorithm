N = int(input())

first_position = 1
result = 1

while N > first_position:
    first_position += 6 * result
    result += 1

print(result)