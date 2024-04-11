import sys
input = sys.stdin.readline

R, C, T = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(R)]
temp = [[0]*C for _ in range(R)]

def diffusion():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(R):
        for j in range(C):
            if room[i][j]

def rotate():
    # 위쪽 순환 : 반시계 방향
    for x in range(cleanerUp - 1,0, -1):
        room[x][0] = room[x-1][0]
    for y in range(C-1):
        room[0][y] = room[0][y+1]
    for x in range(cleanerUp):
        room[x][-1] = room[x+1][-1]
    for y in range(C-1,0,-1):
        room[cleanerUp][y] = room[cleanerUp][y-1]
    
    # 아래쪽 순환 : 시계 방향
    for x in range(cleanerDown+1,R-1):
        room[x][0] = room[x+1][0]
    for y in range(C-1):
        room[-1][y] = room[-1][y+1]
    for x in range(R-1,cleanerDown,-1):
        room[x][-1] = room[x-1][-1]
    for y in range(C-1,0,-1):
        room[cleanerDown][y] = room[cleanerDown][y-1]
        
    room[cleanerUp][1] = 0
    room[cleanerDown][1] = 0
        
for i in range(R):
    if room[i][0] == -1:
        cleanerUp = i
        cleanerDown = i+1
        break
    
rotate()

for i in room:
    print(i)