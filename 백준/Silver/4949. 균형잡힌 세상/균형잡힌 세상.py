# 250220 목 AM 2:03

import sys
input = sys.stdin.readline

answer = []
while True:
    string = input().rstrip()
    if string == '.':
        break
    stack = []
    for s in string:
        if stack:
            if stack[-1] == '(' and s == ')':
                stack.pop()
            elif stack[-1] == '[' and s == ']':
                stack.pop()
            elif s in ('(', ')', '[', ']'):
                stack.append(s)
        elif s in ('(', ')', '[', ']'):
            stack.append(s)
    answer.append('yes' if len(stack) == 0 else 'no')

for i in answer:
    print(i)