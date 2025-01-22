# 250123 목 AM 1:28

import sys
sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

def dfs(idx):
    visited[idx] = True
    print(idx, end = ' ')

    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

def bfs():
    queue = []

    queue.append(V)
    visited[V] = True

    while queue:
        idx = queue.pop(0)
        print(idx, end = ' ')

        for i in range(1, N+1):
            if not visited[i] and graph[idx][i]:
                queue.append(i)
                visited[i] = True

# 0. 입력 및 초기화
N, M, V = map(int, input().split())
graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

# 1. graph에 연결 정보 채우기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

# 2. dfs
dfs(V)
print()

# 3. bfs
visited = [False] * (N+1)
bfs()