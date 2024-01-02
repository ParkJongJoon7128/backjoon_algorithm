n = input()
list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

result = 0  

for i in list:
    for j in i:
        for k in n:
            if(j == k):
                result += list.index(i) + 3

print(result)