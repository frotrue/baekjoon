a, b= map(int, input().split())
while_check = True
if a > b:
    max = a
    min = b
else:
    max = b
    min = a

while while_check:
    t = max%min
    if t == 0:
        print(min)
        while_check = False
        break
    max = min
    min = t

print(a*b//min)