# 250210 월 PM 6:36

import sys
input = sys.stdin.readline

lst = []
for _ in range(5):
    a = int(input())
    lst.append(a)
lst.sort()

print(int(sum(lst)/len(lst)))
print(lst[2])