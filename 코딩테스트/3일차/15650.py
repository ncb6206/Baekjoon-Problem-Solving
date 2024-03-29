import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
array = list()

for i in range(N):
    array.append(i+1)

for j in combinations(array,M):
    print(*j)