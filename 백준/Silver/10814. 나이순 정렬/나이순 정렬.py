import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    age, name = input().split()
    lst.append((int(age), name))

print(*[f"{age} {name}" for age, name in sorted(lst, key=lambda x: x[0])], sep="\n")