arr = []

for _ in range(5):
    arr.append(int(input()))
arr.sort()

avg = sum(arr) // len(arr)
middle_value = arr[len(arr) // 2]

print(avg, middle_value, sep='\n' )