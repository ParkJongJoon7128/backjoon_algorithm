import sys

T = int(sys.stdin.readline().rstrip())
result = []

for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    result.append(A + B)

for i in range(T):
    print(result[i])