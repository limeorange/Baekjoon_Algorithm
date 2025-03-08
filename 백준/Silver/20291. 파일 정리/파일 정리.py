# 250308 토 PM 7:53 / name 정보는 변수에 저장할 필요없음, 기본 dict 사용해서 카운팅

import sys
input = sys.stdin.readline

N = int(input())
dic = dict()
for _ in range(N):
    ex = input().strip().split('.').pop()
    if ex in dic:
        dic[ex] += 1
    else:
        dic[ex] = 1
    
for ex in sorted(dic):
    print(f'{ex} {dic[ex]}')