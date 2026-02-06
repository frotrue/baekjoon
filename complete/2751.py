n = int(input())
arr = []
import sys
input = sys.stdin.readline
print = sys.stdout.write
for i in range(n):
    arr.append(int(input().rstrip()))

arr.sort()
for i in range(n):
    print(str(arr[i]))
    print('\n')