def CNT(N, num):
    cnt = 0
    divN = num
    while N >= divN:
        cnt += (N // divN)
        divN *= num
    return cnt

m, n = map(int, input().split())
print(min(CNT(m, 2)-CNT(n, 2)-CNT(m-n, 2), CNT(m, 5)-CNT(n, 5)-CNT(m-n, 5)))