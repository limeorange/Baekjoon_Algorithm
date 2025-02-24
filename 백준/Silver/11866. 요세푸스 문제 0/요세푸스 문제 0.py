from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N+1))
result = []

while queue:
    queue.rotate(-(K-1))  # K-1번 왼쪽으로 회전
    result.append(queue.popleft())  # K번째 요소 제거

print(f'<{", ".join(map(str, result))}>')