# 250225 화 PM 8:41

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
move = list(map(int, input().split()))
dq = deque()
for i, m in enumerate(move):
    dq.append((i+1, m))

answer = []
while dq:
    idx, num = dq.popleft()
    answer.append(idx)
    if num >= 0:
        dq.rotate(-(num-1))
    else:
        dq.rotate(-num)

print(' '.join(map(str, answer)))