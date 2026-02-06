user_input = input()
a,b = map(int, user_input.split())
best = 0
best_cnt = 0
for _ in range(a):
    user = input()
    cnt = 0
    current = 0
    for i in user:
        if i=="1" and current==0:
            cnt += 1
            current = 1
        elif i=="1" and current==1:
            continue
        else:
            current = 0
    if cnt > best_cnt:
        best_cnt = cnt
        best = 1
    elif cnt == best_cnt:
        best += 1
print(best_cnt)
print(best)
