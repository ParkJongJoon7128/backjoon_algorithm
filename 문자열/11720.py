N = int(input())
n = input()
sum = 0

arr = [int(i) for i in n]

for i in range(len(arr)):
    sum += arr[i]

print(sum)
