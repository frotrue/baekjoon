a = int(input())
b = int(input())
lst = []
for i in range(b):
    if a<=i*i <=b:
        lst.append(i*i)
if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))