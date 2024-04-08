import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
danzi = [list(input().rstrip()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
result = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(idx):
    queue = deque()
    a,b = idx
    queue.append([a,b])
    count = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and danzi[nx][ny] == '1':
                count += 1
                queue.append([nx,ny])
                visited[nx][ny] = True
    result.append(count)            

for i in range(N):
    for j in range(N):
        if danzi[i][j] == '1' and not visited[i][j]:            
            visited[i][j] = True
            bfs([i,j])
                    
print(len(result))
result.sort()
for i in result:
    print(i)