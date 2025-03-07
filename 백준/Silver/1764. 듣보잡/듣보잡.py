import sys
input = sys.stdin.readline

N, M = map(int, input().split())

N_lst = [input().strip() for _ in range(N)]
M_lst = [input().strip() for _ in range(M)]

C= sorted(set(N_lst) & set(M_lst))

print(len(C))
print(*C, sep = '\n')