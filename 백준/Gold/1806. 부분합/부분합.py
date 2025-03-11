# 250312 수 AM 1:35 (15m) / 슬라이딩 윈도우 + 투 포인터

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
s = list(map(int, input().split()))

left, right = 0, 0
current_sum = s[0]
min_length = float('inf')

while right < len(s):
    # 부분합이 S미만인 경우 => right 확장 (right++)
    if current_sum < S:
        right += 1
        if right < len(s):
            current_sum += s[right]
    
    # 부분합이 S이상인 경우
    else:
        if right-left < min_length:
            min_length = right-left
        
        # 부분합 길이가 최소인 구간 탐색
        current_sum -= s[left]
        left += 1

if min_length != float('inf'):
    print(min_length+1)
else:
    print(0)