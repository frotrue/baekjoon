temp  = input()
stack = []
list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0

for i in temp:
    stack.append(i)
    if len(stack)>=2:
        t = ""
        for a in stack:
            t += a
        for j in list:
            if t ==j:
                cnt += 1
                stack = []
                break
        if len(stack)==3:
            cnt +=3

print(cnt)
