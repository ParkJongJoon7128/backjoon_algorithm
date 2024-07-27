H, M = map(int, input().split())

if(H == 0):
    if(M >= 45):
        M -= 45
        print(H, M)
    elif(M < 45):
        H = 23
        M = M + 60 - 45
        print(H, M)
elif(H > 0):
    if(M >= 45):
        M -= 45
        print(H, M)
    elif(M < 45):
        H -= 1
        M = M + 60 - 45
        print(H, M)