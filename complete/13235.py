def check(s):
    if len(s) == 1:
        return "true"
    elif len(s)%2 == 0:
        t1 = s[:len(s)//2]
        t2 = s[len(s)//2:]
        t2 = t2[::-1]
        if t1 == t2:
            return "true"
        else:
            return "false"
    else:
        t3 = s[:(len(s) // 2)]
        t4 = s[(len(s) // 2)+1:]
        t4 = t4[::-1]
        if t3 == t4:
            return "true"
        else:
            return "false"


s = input()
print(check(s))