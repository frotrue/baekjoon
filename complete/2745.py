temp = input()
temp = temp.split(" ")
a = (temp[0])
b = (temp[1])
sum = 0
cnt = 0
for i in range(len(a)-1,-1,-1):
    if a[i].isdigit():
        sum += (int(b)**cnt) * int(a[i])
    else:
        sum += (int(b)**cnt) * (ord(a[i])-55)
    cnt += 1
print(sum)