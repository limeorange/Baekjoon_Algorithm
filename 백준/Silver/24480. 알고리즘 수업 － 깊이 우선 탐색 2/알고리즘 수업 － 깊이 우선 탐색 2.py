import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(idx):
    global graph, answer, visited, order
    
    # DFS가 호출되었다는 것은 해당 노드를 방문한다는 것
    # => 방문 여부, 방문 순서 기록
    visited[idx] = True
    answer[idx] = order
    order += 1

    # 현재 정점과 연결된 인접 정점을 순차적으로 방문
    for i in graph[idx]:
        # 해당 인접 정점이 방문되지 않은 곳이라면 DFS를 호출해서 방문
        if not visited[i]:
            DFS(i)

# 0. 입력 및 초기화
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
answer = [0] * (N+1)
visited = [0] * (N+1)
order = 1

# 1. graph에 연결 정보 채우기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 2. 내림차순 정렬
for i in range(1, N+1):
    graph[i] = sorted(graph[i], reverse=True)

# 3. DFS 호출
DFS(R)

# 4. 정답 출력
for i in range(1, N+1):
    print(answer[i])