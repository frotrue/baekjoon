def temp():
    for i in range(100):
        try:
            a = input()
        except EOFError:
            return
        if a =="":
            return
        print(a)
temp()