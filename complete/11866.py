a,b = map(int,input().split())
arr = list(range(1,a+1))
temp =[]
index = b-1
for _ in range(a-1):
        temp.append(arr[index])
        del arr[index]
        index = index + (b - 1)
        if index >= len(arr):
            index = index % len(arr)

print("<"+", ".join(map(str,temp + arr))+">")