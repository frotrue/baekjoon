n = int(input())
arr= []
for _ in range(n):
    arr.append(input().split(" "))
# print(arr)
sort_list = sorted(arr,key=lambda x:(int(x[0]),int(x[1])))
for i in sort_list:
    print(i[0],i[1])