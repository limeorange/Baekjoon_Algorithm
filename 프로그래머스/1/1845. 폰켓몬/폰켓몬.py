# 250313 목 PM 4:18

def solution(nums):
    unique = set(nums)
    return min(len(nums)//2, len(unique))