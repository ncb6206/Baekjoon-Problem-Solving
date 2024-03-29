import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int,input().split())
array = list()
for i in range(N):
    array.append(i+1)

for dap in permutations(array,M):
    print(*dap)