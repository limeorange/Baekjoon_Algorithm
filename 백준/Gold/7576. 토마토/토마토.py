# 250217 월 PM 11:21

import sys
input = sys.stdin.readline
from collections import deque

def BFS():
    global box, M, N

    # 큐 초기화
    q = deque()

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1: # 익은 토마토 큐에 추가
                q.append((i, j))

    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    
    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni, nj = ci+di[i], cj+dj[i]
            if 0 <= ni < N and 0 <= nj < M:
                if box[ni][nj] == 0: # 익지 않은 토마토가 있는 경우              
                        box[ni][nj] = box[ci][cj] + 1
                        q.append((ni, nj))

    # 탐색 완료 후 조건에 따른 정답 처리
    # 정답 처리 2) 존재하는 토마토가 모두 익지는 못한 경우 => -1
    # 정답 처리 3) 존재하는 토마토가 모두 익은 경우 => 최소 일수
    answer = 0
    for row in box:
        if 0 in row:
            print(-1)
            return
        answer = max(answer, max(row))
    print(answer-1) # 초기값이 1이므로 결과에 -1 해주기
    return
                
# 0. 입력 및 초기화
M, N = map(int, input().split())
box = []
for i in range(N):
    line = list(map(int, input().split()))
    box.append(line)

# 정답처리 1) box에 1, -1만 존재하는 경우 (모든 토마토가 익은 상태) => 0 출력
if all(all(r != 0 for r in row) for row in box):
    print(0)
else:
    # 1. BFS 호출
    BFS()