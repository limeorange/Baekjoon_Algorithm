# 250204 화 PM 8:18

import sys
input = sys.stdin.readline
from collections import deque

def BFS(R):
    global graph, visited, answer
    
    q = deque()
    q.append(R)
    visited[R] = True
    cnt = 0

    while q:
        cur = q.popleft()
        cnt += 1
        answer[cur] = cnt
        # 현재 노드에 인접한 오름차순 노드 중 방문하지 않은 노드 방문 => 너비 우선 탐색
        for i in graph[cur]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

# 0. 입력 및 초기화
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)

# 1. graph에 연결 정보 채우기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 인접 노드 오름차순 정렬
for i in range(1, N+1):
    graph[i].sort()

# 2. BFS 호출
BFS(R)

# 3. 정답 출력
for i in range(1, N+1):
    print(answer[i])