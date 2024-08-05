while True:
    a, b, c = map(int, input().split())

    if(a == b == c == 0):
        break
    else:
        if(a + b + c - max(a, b, c) <= max(a, b, c)):
            print("Invalid")
        else:
            if(a == b == c):
                print("Equilateral")
            elif((a == b) or (b == c) or (c == a)):
                print("Isosceles")
            elif(a != b != c):
                print("Scalene")