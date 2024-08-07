N, M = map(int, input().split())

board = []
result = []

for _ in range(N):
    board.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        line1 = 0
        line2 = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if ((a + b) % 2 == 0):
                    if (board[a][b] != 'B'):
                        line1 += 1
                    elif (board[a][b] != 'W'):
                        line2 += 1
                else:
                    if (board[a][b] != 'W'):
                        line1 += 1
                    elif (board[a][b] != 'B'):
                        line2 += 1
                        
        result.append(line1)
        result.append(line2)

print(min(result))