# 250228 금 PM 8:54

import sys
input = sys.stdin.readline

data = input().split('-')
total = 0

total += sum(map(int, data[0].split('+')))
for i in range(1, len(data)):
    total -= sum(map(int, data[i].split('+')))            
print(total)