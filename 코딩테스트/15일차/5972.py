import sys
from heapq import *
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def dijkstra(start):
    INF = float('inf')
    dist = [INF] * (N+1)
    dist[start] = 0
    queue = [(0,start)]    
    while queue:
        cost, idx = heappop(queue)
        if dist[idx] < cost:
            continue
        
        for adj, d in graph[idx]:
            if dist[adj] > cost + d:
                dist[adj] = cost + d
                heappush(queue,(dist[adj],adj))
    
    return dist

dist = dijkstra(1)   
print(dist[N])