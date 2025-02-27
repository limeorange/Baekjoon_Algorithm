# 250228 금 AM 2:18

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

# 큐인 요소만 합치기 (스택 요소 제거)
q = deque([])
for i, s in enumerate(B):
    if A[i] == 0:
        q.append(s)

# 양방향 큐 활용해서 pop 리턴값 계산
result = []
for item in C:
    q.appendleft(item)
    result.append(q.pop())

print(' '.join(map(str, result)))