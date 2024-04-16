import sys
from heapq import *
input = sys.stdin.readline

T = int(input())        # 테스트 케이스의 개수
result = []             # 각 테스트 케이스의 결과를 저장할 리스트

INF = float('inf')      # 무한대 값 정의

def dikstra(start):
    dist = [INF] * (n+1)    # 각 컴퓨터까지의 최단 거리를 저장할 리스트
    dist[start] = 0         # 시작 컴퓨터까지의 거리는 0
    queue = [(0,start)]     # 우선순위 큐에 시작 컴퓨터와 거리 0을 삽입
    
    # 우선순위 큐가 빌 때까지 반복
    while queue:
        cost,idx = heappop(queue)       # 가장 거리가 짧은 컴퓨터 정보 꺼내기
        # 이미 더 짧은 경로가 존재한다면 무시
        if dist[idx] < cost:            
            continue
        # 현재 컴퓨터에 연결된 인접 컴퓨터 탐색
        for adj, d in graph[idx]:
            if dist[adj] > dist[idx] + d:   # 더 짧은 경로가 발견되었다면 최단 거리 갱신
                dist[adj] = dist[idx] + d
                heappush(queue,(dist[adj],adj))     # 갱신된 거리와 컴퓨터를 큐에 삽입
                
    return dist     # 각 컴퓨터까지의 최단 거리 리턴
    
for _ in range(T):
    n,d,c = map(int,input().split())        # 컴퓨터의 개수, 의존성 개수, 감염된 컴퓨터 번호
    graph = [[] for _ in range(n+1)]        # 각 컴퓨터에 연결된 의존성 정보를 저장할 그래프

    # 의존성 정보 입력받기
    for _ in range(d):
        a,b,s = map(int,input().split())    # a번 컴퓨터가 b번 컴퓨터에 의존하며, s초 후에 감염됨
        graph[b].append([a,s])              # b번 컴퓨터에서 a번 컴퓨터로 가는 간선 추가
    count = 0   # 감염된 컴퓨터 수
    time = 0    # 마지막 컴퓨터가 감염되기까지 걸리는 시간
    
    dist = dikstra(c)   # c번 컴퓨터에서 시작하여 다익스트라 알고리즘 수행
    
    for i in dist:      # 각 컴퓨터까지의 최단 거리 확인
        if i != INF:    # 감염된 컴퓨터라면 감염된 컴퓨터의 수 증가, 최대 감염 시간 갱신
            count += 1 
            time = max(time,i)
            
    result.append([count,time])     # 테스트 케이스의 결과를 리스트에 저장
    
for i in range(T):
    print(*result[i])