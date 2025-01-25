# 250125 토 PM 10:26

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def DFS(y, x):
    global map_

    # 재방문 방지
    map_[y][x] = False

    # 상하좌우 + 대각선 방문할 노드 탐색
    for i in range(8):
        newX = x + dx[i]
        newY = y + dy[i]
        if map_[newY][newX]:
            DFS(newY, newX)

while True:
    
    # 0. 입력 및 초기화
    w, h = map(int, input().split())
    MAX = 50 + 10
    map_ = [[False] * MAX for _ in range(MAX)]
    answer = 0

    if (w, h) == (0, 0):
        break
    
    # 1. map에 연결 정보 채우기
    for y in range(1, h+1):
        row = list(map(int, input().split()))
        for x in range(1, w+1):
            map_[y][x] = (row[x-1] == 1)
    
    # 2. DFS 호출
    for i in range(1, h+1):
        for j in range(1, w+1):
            if map_[i][j]:
                DFS(i, j)
                answer += 1
    
    # 3. 정답 출력
    print(answer)