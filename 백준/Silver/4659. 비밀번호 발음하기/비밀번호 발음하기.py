# 250306 목 PM 8:08 / 코드 성능 최적화 ver. => 불필요한 반복 제거

import sys
input = sys.stdin.readline

mo = {'a', 'e', 'i', 'o', 'u'}
answer = []
while True:
    pwd = input().strip() 
    if pwd == 'end':
        break

    consecutive_mo, consecutive_ja = 0, 0
    rule1, rule2, rule3 = False, True, True
    prev_p = ''

    for i, p in enumerate(pwd):
        
        # 1) 모음(a, e, i, o, u) 하나를 반드시 포함
        if p in mo:
            rule1 = True
            consecutive_mo += 1
            consecutive_ja = 0
        else:
            consecutive_ja += 1
            consecutive_mo = 0
        
        # 2) 모음 or 자음 연속 3개 불가
        if consecutive_mo == 3 or consecutive_ja == 3:
            rule2 = False

        # 3) 같은 글자 연속 불가(ee, oo는 가능)
        if i > 0 and p == prev_p and p not in {'e', 'o'}:
            rule3 = False

        prev_p = p

    if rule1 == rule2 == rule3 == True:
        answer.append(f'<{pwd}> is acceptable.')
    else:
        answer.append(f'<{pwd}> is not acceptable.')

for a in answer:
    print(a)