user = (input())
old = user
if int(user) <10:
    user = "0" + user
while_check = True
cnt = 0
while while_check:
    a = (user[0])
    b = (user[1])
    temp = int(a) + int(b)
    temp = str(temp)
    new_num = str(b)+ (temp[-1])
    if new_num[0] == '0':
        new_num = new_num[1]
    cnt +=1
    if new_num == old:
        while_check = False
        print(cnt)
    else:
        if int(new_num) <10:
            new_num = "0" + new_num
        user = new_num
