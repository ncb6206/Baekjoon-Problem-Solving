# 색약인 경우와 색약이 아닌 경우 두가지를 한번에 구할 수 있는 방법이 있을 것 같은데
# 생각을 하지 못해서 두가지 경우의 dfs를 만들어 구함

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)  # 재귀 깊이 제한을 1,000,000으로 설정

N = int(input())        # 그림의 크기 N 입력받기
picture = [list(input().rstrip()) for _ in range(N)]    # 그림 정보 입력받기

visitedRGB = [[False]*N for _ in range(N)]      # 적록색약이 아닌 경우의 방문 여부 저장
visitedRG = [[False]*N for _ in range(N)]       # 적록색약일 경우의 방문 여부 저장

RGB = 0         # 적록색약이 아닌 사람이 봤을 때의 구역 개수
RG = 0          # 적록색약인 사람이 봤을 때의 구역 개수

# 적록색약이 아닐 경우에 dfs
def dfsRGB(x,y):
    visitedRGB[x][y] = True     # 현재 위치 (x, y) 방문 처리
    
    # 상하좌우 탐색
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        # 탐색한 좌표가 그림 크기안에 있고, 방문을 하지 않았고, 탐색하기 전과 탐색 후의 색깔이 같을 경우 재귀 호출
        if 0 <= nx < N and 0 <= ny < N and not visitedRGB[nx][ny] and picture[x][y] == picture[nx][ny]:
            dfsRGB(nx,ny)            
    
# 적록색약일 경우에 dfs
def dfsRG(x,y,color):
    visitedRG[x][y] = True
    
    # 상하좌우 탐색
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        # 탐색한 좌표가 그림 크기안에 있고, 방문을 하지 않았을 경우에
        if 0 <= nx < N and 0 <= ny < N and not visitedRG[nx][ny]:
            # 탐색하기 전의 색깔이 파란색이고 탐색 후의 색깔이 파란색이면 탐색하는 색깔과 함께 재귀 호출
            if color == 'B':
                if color == picture[nx][ny]:
                    dfsRG(nx,ny,color)
            # 탐색하기 전의 색깔이 파란색이 아니고 탐색 후의 색깔도 파란색이 아니면 탐색하는 색깔과 함께 재귀 호출
            else:
                if picture[nx][ny] != 'B':
                    dfsRG(nx,ny,color)

# 상하좌우 방향 벡터
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    for j in range(N):
        # 적록색약이 아닌 사람이 봤을 때의 구역 개수 세기
        if not visitedRGB[i][j]:
            dfsRGB(i,j)
            RGB += 1
        # 적록색약인 사람이 봤을 때의 구역 개수 세기
        if not visitedRG[i][j]:
            dfsRG(i,j,picture[i][j])
            RG += 1
        
print(RGB, RG)