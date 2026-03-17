n = int(input())
arr = list(map(int, input().split()))
arr.sort()
t = 0
for i in range(n):
    t += sum(arr[:i+1])

print(t)