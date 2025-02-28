# 250228 금 PM 8:08

import sys
input = sys.stdin.readline

N = int(input())
weights = []
for _ in range(N):
    weights.append(int(input()))
weights.sort(reverse=True)

max_weight = 0
for i in range(N):
    if weights[i]*(i+1) > max_weight:
        max_weight = weights[i]*(i+1)

print(max_weight)