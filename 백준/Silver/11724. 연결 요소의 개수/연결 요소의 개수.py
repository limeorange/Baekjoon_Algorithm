import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    global visited, graph
    visited[idx] = True

    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

# 0. 입력 및 초기화
N, M = map(int, input().split())
graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)
answer = 0

# 1. graph에 연결 정보 채우기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True

# 2. DFS 호출
# 연결되어 있는 요소들의 개수를 구할 것이므로 visited가 모두 true 되기 전까지 반복
for i in range(1, N+1):
    if not visited[i]:
        dfs(i) # dfs(1) => 1, 2, 5 / dfs(3) => 3, 4, 6
        answer += 1

# 3. 출력
print(answer)