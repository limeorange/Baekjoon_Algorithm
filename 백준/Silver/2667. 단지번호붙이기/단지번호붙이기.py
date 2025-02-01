N = int(input())
arr = [list(map(int, ' '.join(input()).split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]

def bfs(i, j):
    cnt = 1
    # q 생성 및 초기 데이터 삽입
    q = [(i, j)]
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            # 상하좌우 조건 검사 (범위내, 집 존재, 방문X)
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and v[ni][nj] == 0:
                cnt += 1
                v[ni][nj] = 1
                q.append((ni, nj))
    return cnt

result = []

# 전체 arr 순회
for i in range(N):
    for j in range(N):
        # 집이 있고, 해당 집을 단지로 카운팅 안한 경우
        if arr[i][j] == 1 and v[i][j] == 0:
            v[i][j] = 1
            result.append(bfs(i, j))

result.sort()
print(len(result))
for r in result:
    print(r)