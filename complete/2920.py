user = input()
arr = list(map(int, user.split()))

# print(arr)
temp = sorted(arr)
temp1 = sorted(arr, reverse=True)

if temp == arr:
    print("ascending")
elif temp1 == arr:
    print("descending")
else:
    print("mixed")