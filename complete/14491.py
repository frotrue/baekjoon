n= int(input())
arr = []
while_check = True
while while_check:
    if n//9 > 0:
        arr.append(n%9)
        n //= 9
    else:
        if n != 0:
            arr.append(n)
        while_check = False
        break
arr.reverse()
for i in arr:
    print(i, end="")