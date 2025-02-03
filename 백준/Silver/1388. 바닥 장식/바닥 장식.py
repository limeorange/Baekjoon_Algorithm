# 250203 월 PM 4:39 (20m)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(y, x):
    global map_, visited

    # 재방문 방지
    visited[y][x] = True

    # 방문할 노드 탐색
    if map_[y][x] == '-' and map_[y][x+1] == '-' and not visited[y][x+1]:
        DFS(y, x+1)

    elif map_[y][x] == '|' and map_[y+1][x] == '|' and not visited[y+1][x]:
        DFS(y+1, x)

# 1. 입력 및 초기화
N, M = map(int, input().split())
MAX = 50 + 10
map_ = [[''] * MAX for _ in range(MAX)]
visited = [[False] * MAX for _ in range(MAX)]
answer = 0

# 2. map에 연결 정보 채우기
for i in range(1, N+1):
    line = input().strip()
    for j in range(1, M+1):
        map_[i][j] = line[j-1]

# 3. DFS 호출
for i in range(1, N+1):
    for j in range(1, M+1):
        if not visited[i][j]:
            DFS(i, j)
            answer += 1

# 4. 정답 출력
print(answer)