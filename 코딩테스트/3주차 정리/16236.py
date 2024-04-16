# 이건 그냥 답 봄. 그래도 코드 이해 안됨
# https://aia1235.tistory.com/35

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
size = 2
sharkEat = 0
time = 0    

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(sx,sy):
    global size
    queue = deque()
    queue.append([sx,sy])
    
    visited = [[False] * N for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    eatFish = []
    
    while queue:
        x,y = queue.popleft()        
                
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] <= size:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                queue.append([nx,ny])
                
                if board[nx][ny] < size and board[nx][ny] != 0:
                    eatFish.append([nx,ny,dist[nx][ny]])
                    
    eatFish.sort(key = lambda x: (x[2],x[0],x[1]))
    return eatFish
                
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark_x,shark_y = i,j
            board[i][j] = 0
            break
            
while True:
    fishList = bfs(shark_x,shark_y)
    
    if len(fishList) == 0:
        break
    
    shark_x,shark_y,move_time = fishList[0]
    
    sharkEat += 1
    if size == sharkEat:
        sharkEat = 0
        size += 1
    
    board[shark_x][shark_y] = 0
    time += move_time

print(time)