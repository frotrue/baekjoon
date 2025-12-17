temp  = input()
stack = []
list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0

for i in temp:
    stack.append(i)
    if len(stack)>=2:
        if len(stack)==3:
            t = ""
            for a in stack:
                t += a
            t1 = t[0:2]
            t2 = t[1:3]
            for j in list:
                if t1 == j or t2 == j:
                    cnt += 2
                    stack = []
                    break
                if t==j:
                    cnt += 1
                    stack = []
                    break
        if len(stack)==2:
            t = ""
            for a in stack:
                t += a
            for j in list:
                if t==j:
                    cnt += 1
                    stack = []
                    break
    if len(stack)==3:
        cnt +=1
        stack = stack[1:]


if len(stack)>=1:
    cnt += len(stack)

print(cnt)