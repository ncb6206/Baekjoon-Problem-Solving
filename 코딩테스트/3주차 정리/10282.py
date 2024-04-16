import sys
from heapq import *
input = sys.stdin.readline

T = int(input())
result = []
INF = float('inf')

def dikstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    queue = [(0,start)]
    
    while queue:
        cost,idx = heappop(queue)
        if dist[idx] < cost:
            continue
        
        for adj, d in graph[idx]:
            if dist[adj] > dist[idx] + d: 
                dist[adj] = dist[idx] + d
                heappush(queue,(dist[adj],adj))
                
    return dist
    
for _ in range(T):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append([a,s])
    count = 0
    time = 0
    dist = dikstra(c)
    
    for i in dist:
        if i != INF:
            count += 1
            time = max(time,i)
            
    # print(dist)
    result.append([count,time])
    
for i in range(T):
    print(*result[i])