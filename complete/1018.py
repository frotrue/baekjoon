# using LLM, but use for reference
M, N = map(int, input().split())
board = [input() for _ in range(M)]
result = []

for i in range(M - 7):
    for j in range(N - 7):
        draw1 = 0  # 'W'로 시작하는 경우
        draw2 = 0  # 'B'로 시작하는 경우

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W': draw1 += 1
                    if board[a][b] != 'B': draw2 += 1
                else:
                    if board[a][b] != 'B': draw1 += 1
                    if board[a][b] != 'W': draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))