n = int(input())
import math
for _ in range(n):
    a, b = map(int, input().split())
    print(math.comb(b, a))