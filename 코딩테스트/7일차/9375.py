import sys
import math
from collections import Counter
from itertools import combinations
input = sys.stdin.readline

t = int(input())
result = []

for _ in range(t):
    temp = []
    
    n = int(input())
    for _ in range(n):
        name, type = map(str,input().rstrip().split())
        temp.append(type)
    
    wear = Counter(temp)
    cnt = 1
    for i in wear.values():
        cnt *= i + 1
    
    result.append(cnt-1)
    
for i in result:
    print(i)