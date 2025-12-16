arr = []

for i in range(ord('A'), ord('Z')+1):
    arr.append(0)

maxi = 0
maxcnt = 0
temp = input().upper()
for i in temp:
    arr[ord(i)-65] += 1
for i in range(len(arr)):
    if arr[i] == max(arr):
        maxi = i
        maxcnt += 1

if maxcnt > 1:
    print("?")
else:
    print(chr(maxi+65))