n = int(input())
while_check = True
cnt = 1
while while_check:
    if n == cnt:
        print(cnt)
        while_check = False
        break
    else:
        cnt *= 2