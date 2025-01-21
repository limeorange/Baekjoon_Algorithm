# 250122 수 AM 12:21
# graph: 빈 리스트 활용 ver.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(idx):
    global graph, visited, answer

    # 기본 1) 재방문 방지
    visited[idx] = True

    # 기본 2) 방문할 노드 탐색
    for i in graph[idx]:
        # 방문한 적이 없고, 연결된 노드라면
        if not visited[i]:
            answer += 1
            DFS(i)

# 0. 입력 정보 받기
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = 0

# 1. graph에 연결 정보 채우기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 2. DFS 실행
DFS(1)

# 3. 정답 출력 
print(answer)