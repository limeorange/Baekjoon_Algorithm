# 250203 월 PM 6:07

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(V):
    global graph, visited

    # 재방문 방지
    visited[V] = True

    print(V, end = ' ')

    # 방문할 노드 탐색
    for i in graph[V]:
        if not visited[i]:
            DFS(i)

def BFS(V):
    global graph, visited

    # queue 활용 (FIFO)
    q = []  
    q.append(V)
    visited[V] = True

    while q:
        node = q.pop(0)
        print(node, end = ' ')
        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

# 0. 입력 및 초기화
N, M, V = map(int, input().split())
MAX = N+1
graph = [[] * MAX for _ in range(MAX)]
visited = [False] * MAX

# 1. graph에 연결 정보 채우기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순 정렬
for i in range(1, N+1):
    graph[i] = sorted(graph[i])

# 2. DFS 호출
DFS(V)

# 3. BFS 호출
print()
visited = [False] * MAX
BFS(V)