# 250224 월 PM 6:57

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
deque = deque()
result = []

for _ in range(N):
    data = input().split()
    cmd = data[0]
    
    if cmd == '1':
        deque.appendleft(data[1])
    elif cmd == '2':
        deque.append(data[1])
    elif cmd == '3':
        result.append(deque.popleft() if deque else -1)
    elif cmd == '4':
        result.append(deque.pop() if deque else -1)
    elif cmd == '5':
        result.append(len(deque))
    elif cmd == '6':
        result.append(1 if len(deque)==0 else 0)
    elif cmd == '7':
        result.append(deque[0] if deque else -1)
    elif cmd == '8':
        result.append(deque[-1] if deque else -1)

for r in result:
    print(r)