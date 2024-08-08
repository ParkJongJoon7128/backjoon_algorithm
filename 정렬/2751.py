import sys

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in range(N):
    print(arr[i], sep='\n')