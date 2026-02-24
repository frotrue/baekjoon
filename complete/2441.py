n = int(input())
space = " "
star = "*"
for i in range(n):
    print(space*i,end="")
    print(star*(n-i))