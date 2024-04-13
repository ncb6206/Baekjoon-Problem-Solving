import sys
from collections import deque
input = sys.stdin.readline

# 상, 하, 좌, 우 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
time = 0
size = 2
eat_count = 0

# BFS를 이용해 상어가 먹을 수 있는 물고기를 찾는 함수
def bfs(graph, start, size):
    queue = deque([(start[0], start[1], 0)])  # (행, 열, 거리) 저장
    visited = [[False] * len(graph) for _ in range(len(graph))]
    visited[start[0]][start[1]] = True
    
    INF = float('inf')
    min_distance = INF
    min_x, min_y = INF, INF
    
    while queue:
        x, y, distance = queue.popleft()
        
        # 현재 위치에 있는 물고기가 상어보다 작고, 현재까지의 거리가 최소 거리보다 작다면 갱신
        if 0 < graph[x][y] < size and distance < min_distance:
            min_distance = distance
            min_x, min_y = x, y
        # 현재 위치에 있는 물고기가 상어보다 작고, 현재까지의 거리가 최소 거리와 같다면 행과 열을 비교해 갱신
        elif 0 < graph[x][y] < size and distance == min_distance and (x, y) < (min_x, min_y):
            min_x, min_y = x, y
        
        # 상, 하, 좌, 우 방향으로 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph) and not visited[nx][ny] and graph[nx][ny] <= size:
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))
    
    # 먹을 수 있는 물고기가 없다면 (-1, -1, -1) 반환
    if min_distance == float('inf'):
        return (-1, -1, -1)
    return (min_x, min_y, min_distance)

# 아기 상어의 위치 찾기
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] == 9:
            start = (i, j)
            graph[i][j] = 0
            break

while True:
    # BFS를 이용해 먹을 수 있는 물고기 찾기
    x, y, distance = bfs(graph, start, size)
    
    # 더 이상 먹을 수 있는 물고기가 없다면 종료
    if x == -1:
        break
    
    # 물고기를 먹고 시간 및 크기 업데이트
    time += distance
    eat_count += 1
    graph[x][y] = 0
    
    if eat_count == size:
        size += 1
        eat_count = 0
    
    # 상어의 위치 갱신
    start = (x, y)
    
print(time)