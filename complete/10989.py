n = int(input())
arr = []
arr_count = [0]*10001
import sys
input = sys.stdin.readline
print = sys.stdout.write
for i in range(n):
    arr_count[int(input().rstrip())] += 1

# arr.sort()
for i in range(10001):
    if arr_count[i] != 0:
        for j in range(arr_count[i]):
            print(str(i))
            print('\n')