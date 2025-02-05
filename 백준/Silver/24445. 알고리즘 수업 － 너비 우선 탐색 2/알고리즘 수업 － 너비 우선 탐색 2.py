# 250205 수 PM 9:12

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
        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

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

# 내림차순 정렬
for i in range(1, N+1):
    graph[i].sort(reverse=True)

# 2. BFS 호출
BFS(R)

# 3. 정답 출력
for i in range(1, N+1):
    print(answer[i])