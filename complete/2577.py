a = int(input())
b = int(input())
c = int(input())
temp = a*b*c
temp = str(temp)
for i in range(0,10):
    cnt =0
    for j in range(len(temp)):
        if str(i) == temp[j]:
            cnt +=1

    print(cnt)
