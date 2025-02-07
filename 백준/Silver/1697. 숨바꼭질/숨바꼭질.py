# 250207 금 PM 2:26 => BFS

import sys
input = sys.stdin.readline
from collections import deque

def BFS(N, K):
    global dist
    
    # 큐 초기화
    q = deque()
    q.append(N)
    
    # 재방문 방지
    dist[N] = 0

    while q:
        cur = q.popleft()

        if cur == K:
            return
        
        for n in (cur-1, cur+1, cur*2):
            if 0 <= n <= MAX and dist[n] == 0:
                q.append(n)
                dist[n] = dist[cur]+1            

# 0. 입력 및 초기화
N, K = map(int, input().split())
MAX = 10**6+1
dist = [0] * (MAX * 2)

# 1. BFS 호출
BFS(N, K)

# 2. 정답 출력
print(dist[K])