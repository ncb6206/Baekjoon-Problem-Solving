import sys
input = sys.stdin.readline

N = int(input())
dist = [0] * (N+1)

def pibo(idx):
    for i in range(idx):
        if i == 0:
            dist[i] = 0
        elif i == 1:
            dist[i] = i
        else:
            dist[i] = dist[i-1] + dist[i-2]

pibo(N+1)

print(dist[N])