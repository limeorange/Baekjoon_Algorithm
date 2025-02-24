# 250224 월 PM 6:23

from collections import deque

N, K = map(int, input().split())
q = deque(range(1, N+1))
result = []

while q:
    q.rotate(-(K-1))
    result.append(q.popleft())

print(f'<{', '.join(map(str, result))}>')