import sys

input = sys.stdin.readline
N = int(input())
lst = []

for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))

lst.sort()

for i in lst:
    print(i[0], i[1])