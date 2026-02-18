total = 0
for _ in range(4):
    a,b = map(str,input().split())
    if a=="Es":
        total +=int(b)*21
    else:
        total +=int(b)*17
print(total)