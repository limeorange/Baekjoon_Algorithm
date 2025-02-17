# 250217 월 PM 8:07 (30m)

import sys
input = sys.stdin.readline
from collections import deque

def BFS(si, sj, ei, ej):
    global visited, answer
    
    # 1) 큐 초기화
    q = deque()
    q.append([si, sj])

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    
    while q:        
        ci, cj = q.popleft()

        # 2) 목표 지점에 도달한 경우 탐색 종료
        if (ci, cj) == (ei, ej):
            answer.append(visited[ei][ej])
            return
        
        # 3) 현재 지점에 대해서 방문할 지점 탐색
        for i in range(8):
            ni, nj = ci+dx[i], cj+dy[i]
            if 0 <= ni < I and 0 <= nj < I:
                if visited[ni][nj] == -1:
                    visited[ni][nj] = visited[ci][cj] + 1
                    q.append([ni, nj])


T = int(input())
answer = []
for _ in range(T):

    # 0. 입력 및 초기화
    I = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    visited = [[-1] * I for _ in range(I)]
    visited[si][sj] = 0

    # 1. BFS 호출
    BFS(si, sj, ei, ej)

# 2. 정답 출력
for i in answer:
    print(i)