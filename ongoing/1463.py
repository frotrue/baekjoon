n = int(input())
cnt = 0
while_check = True
while while_check:
    if n%3==0:
        n = n//3
        cnt += 1
    elif n%2==0:
        n = n//2
        cnt += 1
    else:
        n -= 1
        cnt += 1
    if n == 1:
        while_check = False
print(cnt)