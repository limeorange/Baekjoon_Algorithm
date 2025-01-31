# 250131 금 PM 5:54 => map, visited 활용

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(y, x):
    global map_

    # 재방문 방지
    visited[y][x] = True

    # 방문할 노드 탐색
    if map_[y][x] == '-' and map_[y][x+1] == '-':
        DFS(y, x+1)
    elif map_[y][x] == '|' and map_[y+1][x] == '|':
        DFS(y+1, x)

# 0. 입력 및 초기화
N, M = map(int, input().split())
map_ = [[''] * (M+10) for _ in range(N+10)]
visited = [[False] * (M+10) for _ in range(N+10)]
answer = 0

# 1. map에 연결 정보 채우기
for i in range(1, N+1):
    line = input()
    for j in range(1, M+1):
        map_[i][j] = line[j-1]

# 2. DFS 호출
for i in range(1, N+1):
    for j in range(1, M+1):
        if not visited[i][j]:
            DFS(i, j)
            answer += 1

# 3. 정답 출력
print(answer)