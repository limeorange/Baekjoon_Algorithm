import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())
lst = list(map(int, input().split()))

# 고유한 값 정렬
sorted_unique = sorted(set(lst))

# 각 값의 인덱스를 매핑
rank_dict = {value: idx for idx, value in enumerate(sorted_unique)}

# 결과 생성
result = [rank_dict[n] for n in lst]

# 출력
print(' '.join(map(str, result)))
