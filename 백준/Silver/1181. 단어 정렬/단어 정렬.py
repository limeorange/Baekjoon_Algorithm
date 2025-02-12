# 250212 수 PM 7:55

import sys
input = sys.stdin.readline

N = int(input())
lst = [[] for _ in range(51)]

for _ in range(N):
    word = input().strip()
    idx = len(word)
    lst[idx].append(word)

for idx, val in enumerate(lst):
    if len(val) != 0:
        lst[idx] = sorted(set(val))

flatten_lst = sum(lst, [])
for i in flatten_lst:
    print(i)