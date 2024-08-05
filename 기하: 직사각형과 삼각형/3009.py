x_arr = []
y_arr = []

for _ in range(3):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)


for i in range(3):
    if (x_arr.count(x_arr[i]) == 1):
        result_X = x_arr[i]
    if (y_arr.count(y_arr[i]) == 1):
        result_y = y_arr[i]

print(result_X, result_y, end=' ')