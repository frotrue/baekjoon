n = int(input())
arr = []
user = []
user_age = []
user_name = []
for _ in range(n):
    input_user = input()
    temp = input_user.split(" ")
    user.append(temp)
    arr.append(input_user)
    user_age.append(int(temp[0]))
    user_name.append((temp[1]))

# print(user)
sort_list = sorted(user,key=lambda x:int(x[0]))
for i in sort_list:
    print(i[0],i[1])