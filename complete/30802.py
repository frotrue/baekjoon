import math

n = int(input())
arr = list(map(int,input().split(" ")))
arr2 = list(map(int,input().split(" ")))

temp = 0
for i in arr:
    t = int(i)/int(arr2[0])
    t = math.ceil(t)
    temp += t
print(temp)
print(n//arr2[1],n%arr2[1])