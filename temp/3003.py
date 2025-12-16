arr = [1,1,2,2,2,8]

temp = input()
temp = temp.split(" ")
output=""
for i in range(1,7):
    t = arr[int(i)-1] - int(temp[int(i)-1])
    output += str(t) + " "
print(output)