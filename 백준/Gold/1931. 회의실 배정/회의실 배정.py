# 250304 화 AM 1:31 (종료 시간, 시작 시간) 기준 정렬

import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    s, e = map(int, input().split())
    lst.append((s, e))
lst.sort(key = lambda x:(x[1], x[0]))

cnt = 1
end = lst[0][1]
for i in range(1, N):
    if lst[i][0] >= end:
        cnt += 1
        end = lst[i][1]
print(cnt)