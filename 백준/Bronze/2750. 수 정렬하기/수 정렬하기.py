# 250210 월 PM 6:28

import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    a = int(input())
    lst.append(a)
lst.sort()

for i in lst:
    print(i)