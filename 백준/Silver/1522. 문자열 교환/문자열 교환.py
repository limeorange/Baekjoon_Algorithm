# 250311 화 PM 2:55

import sys
input = sys.stdin.readline

string = input().strip()
a_cnt = string.count('a')
cnt = string.count('b')
str_len = len(string)

for i in range(str_len):
    if i < str_len-(a_cnt-1):
        temp_str = string[i:i+a_cnt]
    else:
        temp_str = string[i:] + string[:a_cnt-(str_len-i)]
    cnt = min(cnt, temp_str.count('b'))
print(cnt)