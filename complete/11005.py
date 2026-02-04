user_input = input()
a,b = user_input.split(" ")
a = int(a)
b = int(b)
arr = []
while_check = True
def ascii_retune(num):
    if num <10:
        return num
    else:
        return chr(num-10+ord('A'))
while while_check:
    if a //b != 0:
        arr.append(ascii_retune(a%b))
        a = a//b
    else:
        arr.append(ascii_retune(a%b))
        while_check = False

for i in range(len(arr),0,-1):
    print(arr[i-1],end='')