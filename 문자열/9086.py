n = int(input())

for _ in range(n):
    str = input()
    first_str = str[0]
    last_str = str[len(str) - 1]
    print(first_str + last_str)