# 250212 수 PM 7:32

import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    lst.append((y, x))
lst.sort()

for i in lst:
    print(i[1], i[0])