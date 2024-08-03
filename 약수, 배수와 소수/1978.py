N = int(input())
number_list = list(map(int, input().split()))
sum = 0

for i in number_list:
    for j in range(2, i + 1):
        if(i % j == 0):
            if(i == j):
                sum += 1
            break
        
print(sum)