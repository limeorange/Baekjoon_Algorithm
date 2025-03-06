# 250306 목 PM 7:48

import sys
input = sys.stdin.readline

mo = {'a', 'e', 'i', 'o', 'u'}
answer = []
while True:
    pwd = input().strip()
    if pwd == 'end':
        break

    mo_cnt, ja_cnt = 0, 0
    rule1, rule2, rule3 = True, True, True

    for p in pwd:
        if p in mo:
            mo_cnt += 1
        else:
            ja_cnt += 1

    # 1) 모음(a, e, i, o, u) 하나를 반드시 포함
    if mo_cnt == 0:
        rule1 = False

    # 2) 모음 or 자음 연속 3개 불가
    for i in range(len(pwd)-2):    
        if (pwd[i] in mo) == (pwd[i+1] in mo) == (pwd[i+2] in mo):
            rule2 = False
        elif (pwd[i] not in mo) == (pwd[i+1] not in mo) == (pwd[i+2] not in mo):
            rule2 = False

    # 3) 같은 글자 연속 불가(ee, oo는 가능)
    for i in range(len(pwd)-1):
        if (pwd[i] == pwd[i+1]) and ((pwd[i], pwd[i+1]) not in (('e', 'e'), ('o', 'o'))):
            rule3 = False

    if rule1 == rule2 == rule3 == True:
        answer.append(f'<{pwd}> is acceptable.')
    else:
        answer.append(f'<{pwd}> is not acceptable.')

for a in answer:
    print(a)