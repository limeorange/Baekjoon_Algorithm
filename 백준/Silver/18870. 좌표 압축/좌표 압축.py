# 250215 토 PM 4:36

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

count_dict = dict()
for idx, value in enumerate(sorted(set(lst))):
    count_dict[value] = idx

result = []
for i in lst:
    result.append(count_dict[i])
print(' '.join(map(str, result)))