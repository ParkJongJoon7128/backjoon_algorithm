A, B = map(int, input().split())
C = int(input())

result = B + C
A += result // 60
B = result % 60

if(A > 23):
    A -= 24
print(A, B)