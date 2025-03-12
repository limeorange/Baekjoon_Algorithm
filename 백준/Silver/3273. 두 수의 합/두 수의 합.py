# 250312 수 PM 4:11 / 투 포인터

import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int, input().split()))
x = int(input())

left, right = 0, N-1
current_sum = 0
answer = 0
s.sort()

while left < right:
    current_sum = s[left]+s[right]
    
    if current_sum == x:
        answer += 1
        left += 1
        right -= 1
        
    elif current_sum > x:
        right -= 1

    else:
        left += 1

print(answer)