# 250308 토 PM 7:43

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
dic = defaultdict(int)
for _ in range(N):
    name, ex = map(str, input().strip().rsplit('.', 1))
    dic[ex] += 1

for ex in sorted(dic):
    print(f'{ex} {dic[ex]}')