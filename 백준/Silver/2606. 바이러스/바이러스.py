def dfs(idx):
    global graph, visited
    visited[idx] = True

    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

# 0. 입력 및 초기화
N = int(input()) # 컴퓨터 수
M = int(input()) # 연결 수

# 연결 정보 & 방문 정보 저장
graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

# 1. graph에 연결 정보 채우기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

# 2. dfs(재귀함수) 호출
dfs(1)

# 3. 출력
print(sum(visited)-1)