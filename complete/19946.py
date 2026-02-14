n = int(input())
exponent = 64

while n % 2 == 0:
    n //= 2
    exponent -= 1

print(exponent)