A, B = map(str, input().split())

c1 = int(A[::-1])
c2 = int(B[::-1])

if(c1 > c2):
    print(c1)
else:
    print(c2)