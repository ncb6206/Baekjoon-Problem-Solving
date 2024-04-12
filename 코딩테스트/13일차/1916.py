import sys
from heapq import *
input = sys.stdin.readline


N = int(input())
M = int(input())
bus = [[] for _ in range(N+1)]
for _ in range(M):
    start,end,value = map(int,input().split())
    bus[start].append([end,value])
start,end = map(int,input().split())

def dijkstra(start):
    INF = float('inf')
    dist = [INF] * (N+1)
    dist[start] = 0
    
    queue = [(0,start)]
    while queue:
        cost, idx = heappop(queue)
        if dist[idx] < cost:
            break
            
        for adj,d in bus[idx]:
            if dist[adj] > cost + d:
                dist[adj] = cost + d
                heappush(queue,(dist[adj],adj))
        print(queue,dist)
    
    return dist
                
dist = dijkstra(start)
    
print(dist[end])