n = int(input())
score = 0
for _ in range(n):
    user = input()
    cnt = 1
    for i in range(len(user)):
        if user[i]=="O":
            score += cnt
            cnt += 1
        else:
            cnt = 1
            i = len(user)
    print(score)
    score = 0