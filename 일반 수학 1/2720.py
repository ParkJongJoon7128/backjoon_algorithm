T = int(input())
pay = [0.25, 0.10, 0.05, 0.01]
result = []

for i in range(T):
    rest = int(input())
    rest = float(rest)
    for j in range(len(pay)):
        result.append(rest // (pay[j] * 100))
        rest = rest % (pay[j] * 100)
    
for i in range(len(result)):
    print(int(result[i]), end=' ')