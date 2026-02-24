n = int(input())
for i in range(1,n+1):
    a,b,c = map(int,input().split())
    lst = [a,b,c]
    m = max(lst)
    lst.remove(m)
    if m**2 == lst[0]**2 + lst[1]**2:
        print(f"Scenario #{i}:\nyes\n")
    else:
        print(f"Scenario #{i}:\nno\n")