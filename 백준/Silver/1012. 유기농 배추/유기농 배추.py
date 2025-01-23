import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def DFS(y, x):
    global visited, map_
    visited[y][x] = True

    for i in range(4):
        newY = y + dy[i]
        newX = x + dx[i]
        if map_[newY][newX] and not visited[newY][newX]:
            DFS(newY, newX)

# 0. 입력 및 초기화
T = int(input())
MAX = 50 + 10

while T > 0:
    T -= 1
    M, N, K = map(int, input().split())

    # 1. map에 연결 정보 채우기
    map_ = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]

    for _ in range(K):
        x, y = map(int, input().split())
        map_[y+1][x+1] = True

    # 2. DFS 호출
    answer = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if map_[i][j] and not visited[i][j]:
                DFS(i, j)
                answer += 1

    # 3. 정답 출력
    print(answer)