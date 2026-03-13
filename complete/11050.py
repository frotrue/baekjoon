n,k = map(int,input().split())
import math
print(math.factorial(n) // ((math.factorial(n-k))* (math.factorial(k))))