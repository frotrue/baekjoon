a = int(input())
while_check = True
cnt = 0
a -=1
# if a == 1:
#     print(1)
#     while_check = False
while while_check:
    a -= 6*cnt
    if a > 0:
        cnt += 1
    elif a <= 0:
        print(cnt+1)
        while_check = False