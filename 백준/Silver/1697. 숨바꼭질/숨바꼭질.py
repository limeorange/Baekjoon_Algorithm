# 250217 월 PM 7:21

import sys
input = sys.stdin.readline
from collections import deque

def BFS(N, K):
    global visited, check

    # 1) 큐 초기화
    q = deque()
    q.append(N)

    while q:
        
        # 2) 현재 위치에 대해 방문할 위치 탐색 (3가지)
        cur = q.popleft()

        # 3) 현재 위치가 목표 지점인 경우 탐색 종료
        if cur == K:
            return

        for n in (cur-1, cur+1, cur*2):
            if 0 <= n <= 100000 and visited[n] == -1:
                visited[n] = visited[cur] + 1
                q.append(n)

# 0. 입력 및 초기화
N, K = map(int, input().split())
MAX = 100000 + 1
visited = [-1] * MAX
visited[N] = 0

# 1. BFS 호출
BFS(N, K)

# 2. 정답 출력
print(visited[K])