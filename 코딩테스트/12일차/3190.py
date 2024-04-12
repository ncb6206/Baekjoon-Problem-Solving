# 거의 다 짜다가 마지막에 막혀서 정답을 보았던 문제
# board에 빈 칸, 뱀, 사과를 나누어 주는게 핵심 키 포인트(snake로 판단하려고 했다가 망함)

import sys
from collections import deque,defaultdict
input = sys.stdin.readline

N = int(input())         # 보드의 크기 N x N
K = int(input())         # 사과의 개수
board = [[0]*(N+1) for _ in range(N+1)]     # 보드 정보 저장 (0: 빈 칸, 1: 뱀, 2: 사과)
dir = [0,1]              # 뱀의 진행 방향 (오른쪽)
snake = deque()          # 뱀의 위치 정보 저장
move = defaultdict()     # 방향 전환 시간과 방향 정보 저장

# 사과 정보 입력
for _ in range(K):
    x,y = map(int,input().split())
    board[x][y] = 2    
    
# 방향 전환 정보 입력
L = int(input())
for _ in range(L):
    second,angle = map(str,input().split())
    move[int(second)] = angle    

# 방향 전환 함수
def turn(alpha):
    global dir
    if alpha == 'D':
        dir = nsew[(nsew.index(dir) + 1) % 4]   # 오른쪽으로 90도 회전
    else:
        dir = nsew[(nsew.index(dir) - 1) % 4]   # 왼쪽으로 90도 회전
        
# 상하좌우 방향 정의        
nsew = [[0,1],[1,0],[0,-1],[-1,0]]

# 게임 시작
snake.append([1,1])     # 뱀의 초기 위치
board[1][1] = 1
count = 0               # 게임 시간
while True:
    count += 1
    x,y = snake[-1]     # 뱀의 머리 위치
    nx = x + dir[0]
    ny = y + dir[1]     # 다음 위치
    
    # 게임 종료 조건 체크
    if not(0 < nx <= N and 0 < ny <= N) or board[nx][ny] == 1:
        break
    
    # 사과 먹기
    if board[nx][ny] == 2:
        board[nx][ny] = 1
        snake.append([nx,ny])    
    
    # 빈 칸으로 이동
    elif board[nx][ny] == 0:
        board[nx][ny] = 1
        snake.append([nx,ny])
        px,py = snake.popleft()     # 꼬리 이동
        board[px][py] = 0

    # 방향 전환
    if count in move:
        turn(move[count])
    
print(count)
