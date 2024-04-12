import sys
input = sys.stdin.readline

N = int(input())
dist = [0] * (N+1)

for i in range(1,N+1):
    if i == 1:
        dist[i] = 1
    elif i == 2:
        dist[i] = 2
    else:
        dist[i] = dist[i-1] + dist[i-2]
        
print(dist[N] % 10007)