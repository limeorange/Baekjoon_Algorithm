# 250305 수 PM 7:47

import sys
input = sys.stdin.readline

X, Y, A, B = map(int, input().split())

m = min(X, Y)
M = max(X, Y)

# 1) 직선 / 2) 대각선+직선 
cost = min((X + Y) * A, m * B + (M - m) * A)

# 3) 대각선 이동이 더 이득인 경우 (대각선, 대각선+직선)
if B < 2 * A:
    if (M - m) % 2 == 0: # 대각선 M번 이동
        cost = min(cost, M * B)
    else: # 대각선 M-1번, 직선 1번 이동
        cost = min(cost, (M - 1) * B + A)
print(cost)