# 250219 수 AM 1:24

import sys
input = sys.stdin.readline

T = int(input())
answer = []
for _ in range(T):
    string = list(input().strip())
    stack = []
    for i in range(len(string)):
        if stack and stack[-1] == '(' and string[i] == ')':
            stack.pop()
        else:
            stack.append(string[i])
    answer.append('YES' if len(stack) == 0 else 'NO')

for i in answer:
    print(i)