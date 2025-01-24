# 250125 토 AM 2:29
# visited 없는 버전 (map이 visited 역할 수행)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x):
    global map_, answer, N
    map_[y][x] = False

    if y == N:
        answer = True
        return

    for i in range(4):
        newY = y + dy[i]
        newX = x + dx[i]
        if map_[newY][newX]:
            dfs(newY, newX)

# 0. 입력 및 초기화
N, M = map(int, input().split())
MAX = 1000 + 10
map_ = [[False] * MAX for _ in range(MAX)]

# 1. map에 연결 정보 채우기
for i in range(1, N+1):
    row = input()
    for j in range(1, M+1):
        map_[i][j] = (row[j-1] == "0")

# 2. DFS 호출
answer = False
for j in range(1, M+1):
    if map_[1][j]:
        dfs(1, j)

# 3. 정답 출력
print("YES" if answer else "NO")