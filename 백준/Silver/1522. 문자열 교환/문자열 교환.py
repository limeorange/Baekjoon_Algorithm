# 250311 화 PM 3:05 / 문자열 2배로 이어붙여서 인덱스 설정하는 방식 (효율화)

import sys
input = sys.stdin.readline

ori_string = input().strip()
string = ori_string * 2
a_cnt = ori_string.count('a')
cnt = ori_string.count('b')
str_len = len(ori_string)

for i in range(str_len):
    cnt = min(cnt, string[i:i+a_cnt].count('b'))
print(cnt)