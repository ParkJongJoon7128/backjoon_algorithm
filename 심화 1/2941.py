str = input()
arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in arr:
    str = str.replace(i, "*")

print((len(str)))