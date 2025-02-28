# 241009 수 AM 1:24

N = int(input())
P = map(int, input().split())
P_list = sorted(list(P))

answer = 0
for i in range(1, N+1):
    answer += sum(P_list[:i])
print(answer)