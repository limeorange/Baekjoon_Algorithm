# 250311 화 PM 5:42 / 문자별 인덱스 사전 + 슬라이딩 인덱스 활용

import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    W = input().strip()
    K = int(input())
    
    # 문자별 인덱스 정보 담은 사전 생성
    char_indices = defaultdict(list)
    for i, c in enumerate(W):
        char_indices[c].append(i)
    
    # 1. 각 문자별 등장 인덱스를 활용한 슬라이딩 윈도우 탐색
    min_length = 10001
    max_length = -1
    
    for char, indices in char_indices.items():
        
        # 2. 문자의 개수가 K개 이상인 경우만 고려
        if len(indices) < K:
            continue
    
        # 3. 윈도우 이동하면서 최소, 최대 길이 갱신
        for i in range(len(indices)-K+1):
            length = indices[i+K-1] - indices[i] + 1

            if length < min_length:
                min_length = length
            if length > max_length:
                max_length = length
    
    if min_length == 10001:
        print(-1)
    else:
        print(min_length, max_length)