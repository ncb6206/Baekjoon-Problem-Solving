import sys
from heapq import *
input = sys.stdin.readline

N, M = map(int,input().split())          # 도시의 개수(N)와 도로의 개수(M) 입력받기
graph = [[] for _ in range(N+1)]         # 각 도시에서 연결된 도로 정보를 저장할 그래프

# 도로 정보 입력받기
for _ in range(M):
    a,b,c = map(int,input().split())     # a번 도시와 b번 도시 사이의 거리가 c
    graph[a].append([b,c])               # 도시 a에서 도시 b로 가는 거리가 c인 도로 추가
    graph[b].append([a,c])               # 도시 b에서 도시 a로 가는 거리가 c인 도로 추가

def dijkstra(start):
    INF = float('inf')                   # 무한대 값 정의
    dist = [INF] * (N+1)                 # 각 도시까지의 최단 거리를 저장할 리스트
    dist[start] = 0                      # 시작 도시까지의 거리는 0
    queue = [(0,start)]                  # 우선순위 큐에 시작 도시와 거리 0을 삽입
    
    # 우선순위 큐가 빌 때까지 반복
    while queue:
        cost, idx = heappop(queue)       # 가장 거리가 짧은 도시 정보 꺼내기
        # 이미 더 짧은 경로가 존재한다면 무시
        if dist[idx] < cost:
            continue
        
        # 현재 도시에 연결된 인접 도시 탐색
        for adj, d in graph[idx]:
            # 더 짧은 경로가 발견되었다면 최단 거리 갱신
            if dist[adj] > cost + d:
                dist[adj] = cost + d
                heappush(queue,(dist[adj],adj))     # 갱신된 거리와 도시를 큐에 삽입
    
    # 각 도시까지의 최단 거리 리턴
    return dist

dist = dijkstra(1)      # 1번 도시에서 시작하여 다익스트라 알고리즘 수행
print(dist[N])          # N번 도시까지의 최단 거리 출력