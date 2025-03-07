# 250307 금 PM 5:12 / Counter를 활용한 최적화

import sys
from collections import Counter
input = sys.stdin.readline

N, M = map(int, input().split())
word_counter = Counter()

# 단어 입력 & 빈도수 계산
for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        word_counter[word] += 1

# 단어 정렬 (빈도 내림차순, 길이 내림차순, 알파벳 오름차순)
sorted_words = sorted(word_counter.keys(), key=lambda x: (-word_counter[x], -len(x), x))

print('\n'.join(sorted_words))