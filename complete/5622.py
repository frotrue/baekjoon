a = input()

add = 0

for i in a:
    if i =="S":
        temp = 8
    elif i =="Z":
        temp = 10
    else:
        temp = (ord(i))
        if ord("S")< temp:
            temp -=1
        temp -= 62
        temp //= 3
        temp +=2
    add += temp

print(add)