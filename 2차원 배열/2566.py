arr = []
max_num = 0
max_num_row, max_num_col = 0, 0

for _ in range(9):
    row = list(map(int, input().split()))
    arr.append(row)

for i in range(9):
    for j in range(9):
        if max_num <= arr[i][j]:
            max_num = arr[i][j]
            max_num_row = i + 1
            max_num_col = j + 1

print(max_num)
print(max_num_row, max_num_col)
