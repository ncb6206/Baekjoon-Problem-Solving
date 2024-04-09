import sys
input = sys.stdin.readline

N, M = map(int,input().split())
bridge = [[] for _ in range(N+1)]

for _ in range(M):
    A,B,C = map(int,input().split())
    bridge[A].append([B,C])
    bridge[B].append([A,C])

islandFirst, islandSecond = map(int,input().split())

print(bridge)