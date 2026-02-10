n = int(input())
arr = set()
for _ in range(n):
    arr.add(input())
arr = list(arr)
sort_list = sorted(arr, key=lambda x: (len(x), x))

for i in sort_list:
    print(i)