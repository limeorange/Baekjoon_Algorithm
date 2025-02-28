# N: 동전 종류, K: 동전의 합
N, K = map(int, input().split())

# 동전 종류 리스트로 받기
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse = True)

answer = 0
for coin in coins:
    if coin <= K:
        answer += K//coin
        K -= coin*(K//coin)
print(answer)