# 250307 금 PM 6:38

import sys
input = sys.stdin.readline

S = input().strip()
i = 0 # S의 현재 매칭할 위치
N = 1 # 찾을 자연수

# S의 모든 자릿수를 매칭할 때까지 반복
while i < len(S):
    
    # 현재 자연수를 문자열로 변환한 후, 각 자릿수를 확인
    for ch in str(N): # 1, 2, 3, ..., 10
        
        # 현재 자릿수가 S의 현재 문자와 일치하면 S의 다음 숫자로 이동
        if ch == S[i]:
            i += 1
            
        # 모든 문자 매칭했다면 종료
        if i == len(S):
            print(N)
            break
    N += 1