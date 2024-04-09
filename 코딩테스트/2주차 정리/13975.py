import sys
from heapq import *
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    total = 0
    K = int(input())
    card = list(map(int,input().split()))
    heapify(card)
    
    while len(card) > 1:
        x = heappop(card)
        y = heappop(card)
        hap = x + y
        total += hap
        
        heappush(card,hap)

    result.append(total)
    
for i in result:
    print(i)