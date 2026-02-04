while_check = True
while while_check:
    user_input = input()
    a ,b = map(int, user_input.split())
    if a == 0 and b == 0:
        while_check = False
    else:
        print(a + b)