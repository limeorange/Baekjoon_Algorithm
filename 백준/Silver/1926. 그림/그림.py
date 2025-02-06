from collections import deque

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 세로, 가로
map2 = [list(map(int, input().split())) for _ in range(n)] # 그래프 전체 지도

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(y, x):
    rs = 1
    q = deque()
    q.append((y, x))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if map2[ny][nx] == 1:
                    rs += 1
                    map2[ny][nx] = 2
                    q.append((ny, nx))
    return rs

# [0][0] => [0][1] => ...
cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if map2[j][i] == 1:
            # chk 배열 따로 만들지 않고, 방문이 이루어진 경우 2로 바꿔서 재방문 방지
            map2[j][i] = 2
            cnt += 1
            maxv = max(maxv, bfs(j, i))

print(cnt)
print(maxv)