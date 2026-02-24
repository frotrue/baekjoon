a,b,c = map(int,input().split())
d,h,m = 11,11,11
total_original = d*1440 + h*60 + m
total_new = a*1440 + b*60 + c
if total_new < total_original:
    print(-1)
else:
    print(total_new-total_original)