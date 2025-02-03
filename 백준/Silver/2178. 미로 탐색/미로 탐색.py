N, M = map(int, input().split()) # 세로, 가로
arr = [list(map(int, ' '.join(input()).split())) for _ in range(N)]

def bfs(si, sj, ei, ej):
    q = []
    v = [[0] * M for _ in range(N)]
    
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)

        if (ci, cj) == (ei, ej):
            return v[ei][ej]

        # 4방향(상하좌우)에 대해 조건 검사
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            
            # 1) 범위 내 2) 길이 있고 3) 아직 방문 X
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
    return v[ei][ej]

print(bfs(0, 0, N-1, M-1))