import sys
input = sys.stdin.readline

n1 = int(input())
arr1 = set(map(int,input().split()))
n2 = int(input())
arr2 = list(map(int,input().split()))

for x in arr2:
    if x in arr1:
        print(1)
    else:
        print(0)