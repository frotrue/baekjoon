import re
a = input()
result = re.sub(r'\d', '', a)
b = input()
print(1 if b in result else 0)