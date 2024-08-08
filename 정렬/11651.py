N = int(input())
arr = []    

for _ in range(N):
    x, y = map(int, input().split())
    arr.append((y, x))

new_arr = sorted(arr)

for y, x, in new_arr:
    print(x, y)