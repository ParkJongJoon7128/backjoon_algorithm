list = []

for _ in range(10):
    number = int(input())
    if(number % 42 not in list):
        list.append(number % 42)

print(len(list))