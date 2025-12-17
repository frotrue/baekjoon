num = int(input())
cnt = 0

def one(temp):
    check = 0
    cnt = 0
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[i] == temp[j]:
                return cnt

    if check != 1:
        cnt += 1
    return cnt



for _ in range(num):
    temp = input()
    cnt += one(temp)
print(cnt)