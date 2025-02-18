# 250218 화 PM 12:10

import sys
input = sys.stdin.readline

def stack_order(data):
    global stack, answer
    
    if ' ' in data:
        val = int(data.split()[1])
        stack.append(val)
    elif data == '2':
        if stack:
            answer.append(stack.pop())
        else:
            answer.append(-1)
    elif data == '3':
        answer.append(len(stack))
    elif data == '4':
        if stack:
            answer.append(0)
        else:
            answer.append(1)
    elif data == '5':
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)

N = int(input())
stack = []
answer = []
for _ in range(N):
    data = input().strip()
    stack_order(data)

for i in answer:
    print(i)