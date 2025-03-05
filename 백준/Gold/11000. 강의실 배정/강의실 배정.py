# 250305 수 PM 6:15 / 우선순위 큐 => 힙 자료구조 활용

import sys
import heapq
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    s, e = map(int, input().split())
    lst.append((s, e))
lst.sort(key = lambda x:(x[0]))

heap = [lst[0][1]]
for s, e in lst[1:]:
    if s >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, e)
print(len(heap))