# 250201 토 PM 4:41

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [0, 1]
dx = [1, 0]

def DFS(y, x):
    global map_, visited, N

    # 재방문 방지
    visited[y][x] = True

    if visited[N][N]:
        return

    # 방문할 노드 탐색(우, 하)
    for i in range(2):
        ny = y + (dy[i] * map_[y][x])
        nx = x + (dx[i] * map_[y][x])
        if not visited[ny][nx]:
            DFS(ny, nx)

# 0. 입력 및 초기화
N = int(input())
MAX = 3 + 100 + 10
map_ = [[0] * MAX for _ in range(MAX)]
visited = [[False] * MAX for _ in range(MAX)]

# 1. map에 연결 정보 채우기
for i in range(1, N+1):
    line = list(map(int, input().split()))
    for j in range(1, N+1):
        map_[i][j] = line[j-1]

# 2. DFS 호출
DFS(1, 1)
        
# 3. 정답 출력
print('HaruHaru' if visited[N][N] else 'Hing')