# 1 3 5 11 21
# 1 2 3 5 8

import sys
input = sys.stdin.readline

N = int(input())
dist = [0] * (N+1)

def pibo(idx):
    for i in range(1,idx+1):
        if i == 1:
            dist[i] = 1
        elif i == 2:
            dist[i] = 3
        else:
            dist[i] = dist[i-1] + dist[i-2] * 2
        
pibo(N)

print(dist[N]%10007)
