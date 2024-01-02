N = int(input())
list = list(map(int, input().split()))

M = max(list)
number = []
for i in list:
    number.append(i / M * 100)

average = sum(number)/N
print(average)
