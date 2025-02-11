from sys import stdin, stdout

N = int(stdin.readline())
lst = [0] * 10001

for _ in range(N):
    lst[int(stdin.readline())] += 1

for idx, val in enumerate(lst):
    if val == 0:
        continue
    for _ in range(val):
        stdout.write(f"{idx}\n")