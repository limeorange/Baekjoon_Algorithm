# 250225 화 PM 6:53
# while문을 통해서 이전 단계에서 이미 '간식을 받을 수 있는 학생'이 쌓여있을 가능성 고려

import sys
input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))
stack = []
target = 1

for student in line:
    stack.append(student)
    while stack and stack[-1] == target:
        stack.pop()
        target += 1

print('Nice' if not stack else 'Sad')