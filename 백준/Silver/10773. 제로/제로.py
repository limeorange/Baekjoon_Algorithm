# 250219 수 AM 12:26

import sys
input = sys.stdin.readline

K = int(input())
stack = []
for _ in range(K):
    val = int(input())
    if val == 0:
        stack.pop()
    else:
        stack.append(val)
print(sum(stack))