n = int(input())
for _ in range(n):
    sum = 0
    arr = [0 for i in range(65, 91)]
    s = input()
    for c in s:
        arr[ord(c)-65] += 1
    for i in range(len(arr)):
        if arr[i]==0:
            sum += i+65
    print(sum)