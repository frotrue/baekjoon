n = int(input())

temp = n//5
n = n-(temp*5)
while_check = True
while while_check:
    if n%3==0:
        t = n//3
        temp += t
        while_check = False
        break
    else:
        n +=5
        temp -= 1
        if temp < 0:
            temp = -1
            while_check = False
            break

print(temp)