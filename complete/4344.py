n = int(input())

for _ in range(n):
    temp = input()
    arr = temp.split(" ")
    arr = list(map(int, arr))
    num = int(arr[0])
    sum_num = sum(arr[1:])
    avg_num = sum_num/num
    temp2 = [i for i in arr[1:] if i>avg_num]
    p = len(temp2) / num * 100
    print(f"{p:.3f}%")