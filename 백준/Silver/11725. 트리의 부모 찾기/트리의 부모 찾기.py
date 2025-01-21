# 250121 화 PM 11:20

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(idx):
    global visited, graph, answer

    # 1) 재방문 방지
    visited[idx] = True

    # 2) 방문할 노드 찾기
    for i in graph[idx]:
        if not visited[i]:
            answer[i] = idx # 방문하려는 노드의 부모는 현재 노드
            DFS(i)

# 0. 입력 및 초기화
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)

# 1. graph에 연결 정보 채우기
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 2. DFS 호출
DFS(1)

# 3. 정답 출력
for i in range(2, N+1):
    print(answer[i])