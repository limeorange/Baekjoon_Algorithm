# 250210 월 PM 6:41

import sys
input = sys.stdin.readline

N, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse = True)

print(lst[k-1])