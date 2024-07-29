arr = []

for _ in range(9):
    arr.append(int(input()))

max = max(arr)
max_idx = arr.index(max) + 1

print(max, max_idx, sep='\n')