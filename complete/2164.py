import sys
from collections import deque
queue = deque()
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    queue.append(_+1)
while n > 1:
    queue.popleft()
    temp = queue[0]
    queue.popleft()
    queue.append(temp)
    n -= 1
print(queue[0])