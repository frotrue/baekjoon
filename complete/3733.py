while True:
    try:
        user_input = input()
        a, b = map(int, user_input.split())
        a += 1
        print(b//a)
    except EOFError:
        break