n = int(input())
arr = []
easy_index = 0
hard_index = 0
for _ in range(n):
    n = int(input())
    arr.append(n)

sort_arr = sorted(arr)
if sort_arr[0]==arr[0]:
    easy_index = 1
if sort_arr[-1]==arr[0]:
    hard_index = 1

if easy_index ==1:
    print("ez")
elif hard_index ==1:
    print("hard")
else:
    print("?")