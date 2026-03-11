n,m = map(int,input().split())
board = [[i for i in range(n)] for _ in range(m)]
for i in range(n):
    board[i] = list(map(str,input().split()))
cnt =0
if board[0][0][0] == "W":
    for i in range(0,n):
        for j in range(0,m):
            if (j%2==0)and (i%2==0) and (board[i][j] == "W"):
                continue
            else:
                cnt+=1
elif board[0][0][0] == "B":
    for i in range(0,n):
        for j in range(0,m):
            if (j%2==0)and (i%2==0) and (board[i][j] == "B"):
                continue
            else:
                cnt+=1

print(cnt)
print(board[0][0][0])
print(board)