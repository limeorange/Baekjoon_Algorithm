# 250308 토 PM 6:35
# 성능 최적화 => 1) half => 리스트 append 후 ''.join() / 2) 함수로 만들기

import sys
from collections import Counter
input = sys.stdin.readline

def make_palindrome(data):

    # 팰린드롬 가능 여부 => unique 문자 1) 짝수 n개 / 2) 홀수 1개, 짝수 n-1개
    counter = Counter(data)
    h_cnt = 0
    h_char = ''
    for c in counter:
        if counter[c] % 2 == 1:
            h_cnt += 1
            h_char = c
            counter[c] -= 1 # 팰린드롬의 중심에 홀수개에 해당하는 문자가 놓일 예정
        if h_cnt == 2:
            return("I'm Sorry Hansoo")

    # 팰린드롬 만들기
    half = []
    for c in sorted(counter.keys()): # Counter key 기준 '정렬'한 후 하나씩 순회해야 함
        half.append(c * (counter[c]//2))
    return ''.join(half) + h_char + ''.join(reversed(half))

data = input().strip()
print(make_palindrome(data))