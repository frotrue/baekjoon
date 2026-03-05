import sys
input = sys.stdin.readline

n,m = map(int,input().split())
n_arr = set()
m_arr = set()
for _ in range(n):
    n_arr.add(input())
for _ in range(m):
    t = input()
    if t in n_arr:
        m_arr.add(t)
print(len(m_arr))
m_arr = sorted(m_arr)
for t in m_arr:
    if t == "":
        continue
    print(t,end="")

