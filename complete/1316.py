result = int(input())
for _ in range(result):
    tmp = []
    for s in input():
        if s not in tmp:
            tmp.append(s)
        else:
            if tmp[-1] != s:
                result -= 1
                break
print(result)