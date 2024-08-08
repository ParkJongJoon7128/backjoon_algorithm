import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

new_arr = sorted(list(set(arr)))

dic = {}

for i in range(len(new_arr)):
    dic[new_arr[i]] = i

for j in arr:
    print(dic[j], end=' ')  
