import sys
from collections import deque
input = sys.stdin.readline

T = int(input())        # 테스트 케이스의 수 T 입력받기
result = []             # 각 테스트 케이스의 결과를 저장할 리스트

# 나이트의 이동 가능한 방향 벡터
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

# 정답 보고 수정한 코드
# python으로 돌렸을 때 : 3028ms, pypy로 돌렸을 때 : 312ms
for _ in range(T):
    I = int(input())                             # 체스판의 크기 I 입력
    current = list(map(int,input().split()))     # 나이트의 처음 위치 입력
    arrive = list(map(int,input().split()))      # 나이트가 도착해야 할 위치 입력
    
    queue = deque()                              # 큐 자료구조 생성    
    move = [[0]*I for _ in range(I)]             # 각 칸까지의 최소 이동 횟수 저장
    
    queue.append(current)                        # 처음 위치를 큐에 삽입    
    while queue:
        x,y = queue.popleft()                    # 큐에서 현재 위치 꺼내기
        
        if x == arrive[0] and y == arrive[1]:    # 도착점에 도달한 경우
            result.append(move[x][y])            # 최소 이동 횟수 결과 리스트에 저장
            break
        
        for i in range(8):                       # 나이트의 8가지 이동 가능 방향 확인
            nx = x + dx[i]
            ny = y + dy[i]
            # 새로운 위치가 체스판 내부이고 아직 방문하지 않은 경우
            if 0 <= nx < I and 0 <= ny < I and move[nx][ny] == 0:
                move[nx][ny] = move[x][y] + 1    # 현재 위치까지 이동한 횟수에 1을 더한 값을 저장
                queue.append([nx,ny])            # 새로운 위치를 큐에 삽입
    
for i in result:
    print(i)
    
# python으로 돌렸을 땐 시간 초과가 났지만 pypy로 돌렸을 땐 맞춘 알고리즘
# while안에 if문 분기 처리 때문에 시간초과가 떴던거 같다
# python으로 돌렸을 때 : 시간초과, pypy로 돌렸을 때 : 444ms
# for _ in range(T):
#     I = int(input())
#     current = list(map(int,input().split()))
#     arrive = list(map(int,input().split()))
#     queue = deque()   
#     minCount = 10 ** 9
    
#     if current[0] == arrive[0] and current[1] == arrive[1]:
#         result.append(0)
#         continue
    
#     move = [[0]*I for _ in range(I)]
#     queue.append(current)
    
#     while queue:
#         cur = queue.popleft()
#         x,y = cur
#         for i in range(8):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < I and 0 <= ny < I and move[nx][ny] == 0:
#                 move[nx][ny] = move[x][y] + 1
#                 if nx == arrive[0] and ny == arrive[1]:
#                     minCount = min(minCount,move[nx][ny])
#                     break
#                 else:
#                     queue.append([nx,ny])

#     result.append(minCount)
