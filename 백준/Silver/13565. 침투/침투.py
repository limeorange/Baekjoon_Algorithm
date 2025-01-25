# 250125 토 PM 9:41 => visited 없는 ver.

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(y, x):
    global map_, answer
    
    # 재방문 방지
    map_[y][x] = False

    if y == M:
        answer = True
        return

    # 상하좌우 방문할 노드 탐색
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if map_[newY][newX]:
            DFS(newY, newX)

# 0. 입력 및 초기화
M, N = map(int, input().split())
MAX = 1000 + 10
map_ = [[False] * MAX for _ in range(MAX)]
answer = False

# 1. map에 연결 정보 채우기
for y in range(1, M+1):
    row = input()
    for x in range(1, N+1):
        map_[y][x] = (row[x-1] == '0')

# 2. DFS 호출
for i in range(1, N+1):
    if map_[1][i]:
        DFS(1, i)

# 3. 정답 출력
print("YES" if answer else "NO")