# 결국 정답 본 거 이거 정답 안봤으면 절대 못 풀었을듯...

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().rstrip().split()))
nge = [-1]*n
stack = [0]

for i in range(1,n):
    while stack and a[stack[-1]] < a[i]:
        nge[stack.pop()] = a[i]
    stack.append(i)
    
print(*nge)