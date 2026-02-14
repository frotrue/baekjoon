n = int(input())
arr = []
user_input = input().split(" ")
for i in range(1,n+1):
    temp = user_input[i-1]
    if i==1:
        arr.append(i)
    else:
        if temp == 0:
            arr.append(i)
        else:
            arr.insert(len(arr)-int(temp), i)
for i in arr:
    print(i, end=" ")