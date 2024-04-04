import sys
import math
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
result = []

for _ in range(t):
    wear = defaultdict(int)
    
    n = int(input())
    for _ in range(n):
        name, type = map(str,input().rstrip().split())
        wear[type] += 1
        
    cnt = 1
    for i in wear.values():
        cnt *= i + 1
    
    result.append(cnt-1)
    
for i in result:
    print(i)