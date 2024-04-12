import sys
from heapq import *
input = sys.stdin.readline

N = int(input())    # 도시의 개수
M = int(input())    # 버스의 개수

# 버스의 출발 도시, 도착 도시 번호, 버스 비용 정보 입력받아 그래프에 추가
bus = [[] for _ in range(N+1)]
for _ in range(M):
    start,end,value = map(int,input().split())
    bus[start].append([end,value])
    
# 출발 도시와 도착 도시 번호 입력받기
start,end = map(int,input().split())

def dijkstra(start):
    INF = float('inf')          # 무한대 값 설정
    dist = [INF] * (N+1)        # 출발 도시부터 각 도시까지의 최단 거리 비용을 저장할 리스트
    dist[start] = 0             # 출발 도시의 거리비용은 0으로 초기화
    
    queue = [(0,start)]         # (거리비용, 도시 번호) 형태로 우선순위 큐 생성
    
    while queue:
        cost, idx = heappop(queue)      # 거리비용이 가장 짧은 도시 꺼내기
        if dist[idx] < cost:            # 최단 거리 비용보다 거리비용이 큰 도시라면 continue
            continue
            
        for adj,d in bus[idx]:          # 현재 도시에서 갈 수 있는 인접 도시 확인
            # 현재 거리의 거리 비용보다 새로운 거리의 거리 비용이 더 작다면 최단 거리 비용 업데이트
            if dist[adj] > cost + d:                
                dist[adj] = cost + d                
                heappush(queue,(dist[adj],adj))     # 큐에 새로운 도시의 거리 비용과 도시 번호 추가
    
    # 각 도시의 최단 거리 비용을 저장한 리스트 반환
    return dist

# 출발도시를 기준으로 다익스트라 알고리즘 수행                
dist = dijkstra(start)

# 출발도시부터 도착 도시까지의 최단 거리 출력
print(dist[end])