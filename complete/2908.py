temp = input()
temp = temp.split(" ")
a = (temp[0])
b = (temp[1])
a = a[::-1]
b = b[::-1]
if a > b:
    print(a)
else:
    print(b)