a,b,c = map(int,input().split())
for _ in range(c):
    if a>b*2 or a<b:
        b -= 1
    else:
        a-=1
temp1 =a//2
temp2 =b
print(temp1) if temp1<temp2 else print(temp2)