# 250303 월 PM 11:50

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    lst = []
    N = int(input())
    for _ in range(N):
        x, y = map(int, input().split())
        lst.append((x, y))
    lst.sort()
    
    cnt = 0
    y_min = lst[0][0]
    for i in range(len(lst)):
        if i == 0:
            y_min = lst[i][1]
            cnt += 1
        elif y_min > lst[i][1]:
            cnt += 1
            y_min = lst[i][1]
    print(cnt)