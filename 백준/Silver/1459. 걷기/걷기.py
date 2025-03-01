X, Y, A, B = map(int, input().split())

# 작은 값 m, 큰 값 M
m = min(X, Y)
M = max(X, Y)

# 가능한 경우의 최소 비용 계산
cost = min((X + Y) * A, m * B + (M - m) * A)

# 대각선 이동이 더 이득일 때 처리
if B < 2 * A:
    if (M - m) % 2 == 0:
        cost = min(cost, M * B)
    else:
        cost = min(cost, (M - 1) * B + A)

print(cost)
