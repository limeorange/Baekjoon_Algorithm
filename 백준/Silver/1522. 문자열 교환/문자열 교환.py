# 250311 화 PM 3:06 / 문자열 2배로 이어붙여서 인덱스 설정하는 방식 (초간단)

import sys
input = sys.stdin.readline

string = input().strip()
a_cnt = string.count('a')
cnt = 1000
S = string*2

for i in range(len(string)):
    cnt = min(cnt, S[i:i+a_cnt].count('b'))
print(cnt)