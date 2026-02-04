user_input = input()
user_input = user_input.split(" ")
a,b,c = int(user_input[0]),int(user_input[1]),int(user_input[2])
if (c-a)%(a-b) != 0:
    print((c-a)//(a-b)+2)
else:
    print(int((c-a)/(a-b)+1))