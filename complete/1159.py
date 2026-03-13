n = int(input())
str_arr = []
for _ in range(n):
    str_arr.append(input()[0])
temp = list(set(str_arr))
t = []
for _ in range(len(temp)):
    if str_arr.count(temp[_])>=5:
        t.append(temp[_])


if len(t)==0:
    print("PREDAJA")
else:
    t.sort()
    for i in t:
        print(i, end="")