from collections import Counter
n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
# for _ in range(m):
#     print(n_arr.count(m_arr[_]), end=" ")
Counters = Counter(n_arr)
for _ in range(m):
    print(Counters[m_arr[_]], end=" ")