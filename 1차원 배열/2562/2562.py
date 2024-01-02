list = []

for i in range(1, 10):
    number = int(input())
    list.append(number)

print(max(list))
print(list.index(max(list)) + 1)