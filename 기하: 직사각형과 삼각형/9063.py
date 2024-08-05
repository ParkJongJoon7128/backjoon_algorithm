N = int(input())

x_arr = []
y_arr = []

for _ in range(N):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)

width = max(x_arr) - min(x_arr)
height = max(y_arr) - min(y_arr)

if(len(x_arr) > 1 and len(y_arr) > 1):
    print(width * height)
else:
    print(0)