# 250312 수 PM 8:17 / 슬라이딩 윈도우 + 투포인터

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
s = list(map(int, input().split()))

count = {}
left, max_length = 0, 0

for right in range(N):
    count[s[right]] = count.get(s[right], 0) + 1

    while count[s[right]] > K:
        count[s[left]] -= 1
        left += 1
    max_length = max(max_length, right-left+1)
    
print(max_length)