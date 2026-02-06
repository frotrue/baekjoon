import sys

input = sys.stdin.readline

n = int(input())

def my_round(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)

percent = n*(15/100)
percent = my_round(percent)
arr = []
if n==0:
    print(0)
else:
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    arr = arr[percent:n-percent]
    add = 0
    for i in arr:
        add += int(i)
    print(my_round(add/len(arr)))