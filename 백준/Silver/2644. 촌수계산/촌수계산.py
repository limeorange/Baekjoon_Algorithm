# 250121 화 PM 6:58
# graph => 2차원 배열이 아닌 빈 리스트 활용 ver.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(idx, count):

    global end, graph, visited, answer
    
    # 기본 1) 재방문 방지
    visited[idx] = True

    # 추가 1) 방문한 노드가 목표 노드(end)인 경우
    if idx == end:
        answer = count
        return
    
    # 기본 2) 방문할 노드 찾기
    for i in graph[idx]:
        # 방문한 적이 없고 연결되어 있다면
        if not visited[i]:
            DFS(i, count+1)

# 0. 입력 및 초기화
N = int(input())
start, end = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
answer = -1

# 1. graph에 연결 정보 채우기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 2. DFS 호출
DFS(start, 0)

# 3. 정답 출력
print(answer)