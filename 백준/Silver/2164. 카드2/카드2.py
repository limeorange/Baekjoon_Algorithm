# 250221 금 AM 1:37

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
cards = deque(range(1, N+1))
while True:
    if len(cards) == 1:
        print(cards[0])
        break
    cards.popleft()
    cards.append(cards.popleft())