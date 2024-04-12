import sys
input = sys.stdin.readline

R, C, T = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(R)]
beforeRoom = room[:]    # 미세먼지 확산과 공기청정기 작동 전 현재 방 상태 저장

# 공기청정기 위치 찾기
for i in range(R):
    if room[i][0] == -1:
        cleanerUp = i       # 위쪽 공기청정기 위치
        cleanerDown = i+1   # 아래쪽 공기청정기 위치
        break

# 미세먼지 확산 함수
def diffusion():
    dx = [1,-1,0,0]         # 상하좌우 4방향
    dy = [0,0,1,-1]
    
    for y in range(R):
        for x in range(C):
            if beforeRoom[y][x] > 0:    # 현재 방에 미세먼지가 있는 경우
                count = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    # 탐색한 좌표가 방안에 있고 공기청정기가 아닌 경우에 빈 공간을 이용하여 새로운 값 저장
                    if 0 <= ny < R and 0 <= nx < C and beforeRoom[ny][nx] != -1:
                        temp[ny][nx] += (beforeRoom[y][x] // 5)     # 확산
                        count += 1   # 확산된 방 카운트
                temp[y][x] += beforeRoom[y][x] - (beforeRoom[y][x] // 5) * count    # 원래 위치의 미세먼지 양 업데이트
    
    # 공기청정기 위치 -1로 표시
    temp[cleanerUp][0] = -1
    temp[cleanerDown][0] = -1

# 공기 청정기 작동 함수 (이 부분만 정답을 참고하였음)
def rotate():
    # 위쪽 순환 : 반시계 방향
    for x in range(cleanerUp - 1,0, -1):
        temp[x][0] = temp[x-1][0]
    for y in range(C-1):
        temp[0][y] = temp[0][y+1]
    for x in range(cleanerUp):
        temp[x][-1] = temp[x+1][-1]
    for y in range(C-1,0,-1):
        temp[cleanerUp][y] = temp[cleanerUp][y-1]
    
    # 아래쪽 순환 : 시계 방향
    for x in range(cleanerDown+1,R-1):
        temp[x][0] = temp[x+1][0]
    for y in range(C-1):
        temp[-1][y] = temp[-1][y+1]
    for x in range(R-1,cleanerDown,-1):
        temp[x][-1] = temp[x-1][-1]
    for y in range(C-1,0,-1):
        temp[cleanerDown][y] = temp[cleanerDown][y-1]
    
    # 공기청정기 바로 앞부분의 미세먼지 0 처리        
    temp[cleanerUp][1] = 0
    temp[cleanerDown][1] = 0        


# T초 동안 반복
for _ in range(T):
    temp = [[0]*C for _ in range(R)]    # 1초마다 방에 남아있는 미세먼지 양을 저장하는 위한 빈 공간 생성
    total = 0
    diffusion()     # 미세먼지 확산
    rotate()        # 공기청정기 작동
    beforeRoom = temp[:]    # 현재 방 상태를 저장
    for i in temp:
        total += sum(i) # 현재 방에 남아있는 총 미세먼지 양 계산

print(total + 2)    # 공기청정기로 인해 2를 더하여 출력