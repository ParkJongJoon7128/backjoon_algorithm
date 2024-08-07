N = int(input())

number = 666
result = 0

while True:
    if ('666' in str(number)):
        result += 1
    if (result == N):
        print(number)
        break
    number += 1
