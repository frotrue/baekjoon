n = int(input())
for _ in range(n):
    user_input = input()
    if len(user_input)!=7:
        print(0)
        continue
    else:
        if len(set(user_input))!=2:
            print(0)
            continue
        else:
            if user_input[0]==user_input[1]==user_input[4]:
                print(1)
            else:
                print(0)