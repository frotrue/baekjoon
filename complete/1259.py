def check(s):
    if len(s) == 1:
        return "yes"
    elif len(s)%2 == 0:
        t1 = s[:len(s)//2]
        t2 = s[len(s)//2:]
        t2 = t2[::-1]
        if t1 == t2:
            return "yes"
        else:
            return "no"
    else:
        t3 = s[:(len(s) // 2)]
        t4 = s[(len(s) // 2)+1:]
        t4 = t4[::-1]
        if t3 == t4:
            return "yes"
        else:
            return "no"


while_check = True
while while_check:
    s = input()
    if s == "0":
        while_check = False
        break
    print(check(s))