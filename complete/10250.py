n = int(input())

for _ in range(n):
    h = 1
    w = 1
    a, b, c = map(int, input().split())
    if a==1 and b ==1 and c==1:
        print('101')
        continue
    for i in range(c-1):
        if h==a:
            h = 1
            w += 1
        else:
            h += 1
    print(h, end='')
    if len(str(w))==1:
        w = '0'+str(w)
    print(w)
