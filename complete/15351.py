n = int(input())
for _ in range(n):
    score = 0
    user_input = input()
    for char in user_input:
        if char ==" ":
            continue
        score +=ord(char)-64
    print("PERFECT LIFE")if score ==100 else print(score)