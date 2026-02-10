from itertools import *

a,b = map(int,input().split())
arr = list(map(int,input().split()))
printList = list(combinations(arr, 3))
max_nums = (0,0,0)
for i in printList:
    if sum(max_nums) < sum(i) <= b:
        max_nums = i

print(sum(max_nums))