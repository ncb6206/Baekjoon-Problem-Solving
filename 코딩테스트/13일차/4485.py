import sys
from heapq import *
input = sys.stdin.readline

result = []     # 결과를 저장할 리스트

# 상하좌우로 이동할 수 있는 네 방향
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dijkstra(x,y):
    INF = float('inf')      # 무한대 값 설정
    dist = [[INF]*N for _ in range(N)]       # 각 칸까지의 최소 비용을 저장할 리스트
    
    # 시작 칸의 비용을 0으로 초기화하고 우선순위 큐에 넣기
    queue = []
    heappush(queue, [jido[x][y],x,y])
    dist[x][y] = jido[x][y]
    
    while queue:
        cost, tx, ty = heappop(queue)    # 비용이 가장 작은 칸 꺼내기
        
        # 상하좌우로 이동할 수 있는 칸 확인
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                 # 새로운 칸의 비용이 현재 비용 + 새로운 칸의 비용보다 크다면
                if dist[nx][ny] > cost + jido[nx][ny]:
                    dist[nx][ny] = cost + jido[nx][ny]      # 비용 업데이트
                    heappush(queue,[dist[nx][ny],nx,ny])    # 큐에 새로운 칸 추가
    
    return dist

while True:
    N = int(input())
    if N == 0:  # 0이 입력되면 종료
        break
    
    # 지도 정보 입력받기
    jido = [list(map(int,input().split())) for _ in range(N)]
    
    # 다익스트라 알고리즘 수행하여 도착 지점까지의 최소 비용 계산
    dist = dijkstra(0,0)
    result.append(dist[N-1][N-1]) 

# 결과 출력
for i in range(len(result)):
    print(f"Problem {i+1}: {result[i]}")