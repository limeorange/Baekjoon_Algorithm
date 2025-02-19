# 250220 목 AM 2:20

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque()
for _ in range(N):
    data = input()
    order = data.split()[0]
    if order == 'push':
        queue.append(data.split()[1])
    elif order == 'pop':
        print(queue.popleft() if queue else -1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif order == 'front':
        print(queue[0] if queue else -1)
    elif order == 'back':
        print(queue[-1] if queue else -1)