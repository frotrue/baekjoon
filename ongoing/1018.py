m,n = map(int,input().split())
board = []
for i in range(m):
    board.append(list(input()))
cnt =0
t = board[0]
# correct_arr = []
if t[0]=="W":
    correct_arr = ['W' if i % 2 == 0 else 'B' for i in range(n)]
    correct_arr2 = ['B' if i % 2 == 0 else 'W' for i in range(n)]
else:
    correct_arr = ['B' if i % 2 == 0 else 'W' for i in range(n)]
    correct_arr2 = ['W' if i % 2 == 0 else 'B' for i in range(n)]
for i in range(m):
    if i%2==0 and board[i]==correct_arr[i]:
        continue
    elif i%2==1 and board[i]==correct_arr2[i]:
        continue
    else:
        temp = board[i]
        if i%2==0:
            cnt +=sum(1 for a, b in zip(temp, correct_arr) if a != b)
        if i%2==1:
            cnt += sum(1 for a, b in zip(temp, correct_arr2) if a != b)

# print(board)
print(cnt)
#TODO 일단 개수까지는 만들었는데 정사각형은 생각못하겠음. 나중에 재고해보기