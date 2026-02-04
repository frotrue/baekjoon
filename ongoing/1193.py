user_input = int(input())

while_check = True
cnt =1
while while_check:
    if user_input-cnt <=0:
        print(cnt)
        print(user_input)
        while_check = False
    else:
        user_input -= cnt
        cnt +=1
