import sys
from collections import deque
input = sys.stdin.readline

# 필드의 크기
rows, cols = 12, 6

# 상하좌우 4방향 이동을 위한 델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 주어진 field에서 (r, c) 위치의 같은 색 뿌요를 찾아 삭제하는 BFS 함수
def bfs(field, r, c, color):    
    queue = deque([(r, c)])             # 큐를 생성하고, (r, c) 좌표를 큐에 넣음    
    visited = set()                     # 방문한 좌표를 저장할 집합 생성    
    puyos = [(r, c)]                    # 삭제할 뿌요의 좌표를 저장할 리스트 생성

    # 큐가 빌 때까지 반복
    while queue:        
        row, col = queue.popleft()      # 큐에서 좌표를 꺼냄        
        visited.add((row, col))         # 방문 표시

        # 상하좌우 4방향으로 탐색
        for i in range(4):
            new_r, new_c = row + dr[i], col + dc[i]
            # 새로운 좌표가 필드 범위 내이고, 같은 색이며, 아직 방문하지 않았다면
            if 0 <= new_r < rows and 0 <= new_c < cols and field[new_r][new_c] == color and (new_r, new_c) not in visited:
                # 큐에 추가하고, puyos 리스트에 좌표 추가
                queue.append((new_r, new_c))
                puyos.append((new_r, new_c))

    # puyos 리스트의 길이가 4 이상이면 해당 뿌요들을 모두 삭제하고 True 반환
    if len(puyos) >= 4:
        for r, c in puyos:
            field[r][c] = '.'
        return True
    # 그렇지 않으면 False 반환
    return False

# 필드에 중력을 적용하여 뿌요들을 내리는 함수
def gravity(field):
    # 각 열에 대해 반복
    for c in range(cols):        
        stack = []          # 스택 생성
        # 아래에서부터 위로 탐색
        for r in range(rows-1, -1, -1):
            # 뿌요가 있다면 스택에 추가하고, 해당 칸을 '.'으로 바꿈
            if field[r][c] != '.':
                stack.append(field[r][c])
                field[r][c] = '.'
        # 다시 아래에서부터 위로 탐색하며 스택의 값을 필드에 넣음
        for r in range(rows-1, -1, -1):
            if stack:
                field[r][c] = stack.pop()
            else:
                field[r][c] = '.'

# 한 번의 뿌요 뿌요 게임을 진행하는 함수
def play_puyo(field):   
    score = 0                    # 점수 초기화
    # 더 이상 제거할 뿌요가 없을 때까지 반복
    while True:        
        is_popped = False        # 뿌요가 제거되었는지 여부
        # 필드의 모든 칸을 탐색
        for r in range(rows):
            for c in range(cols):
                # 빈 칸이 아닌 경우
                if field[r][c] != '.':
                    # bfs 함수를 호출하여 뿌요를 제거하고, 점수 증가
                    if bfs(field, r, c, field[r][c]):
                        is_popped = True
                        score += 1
        # 더 이상 제거할 뿌요가 없다면 반복 종료
        if not is_popped:
            break        
        gravity(field)          # 중력 적용    
    return score                # 최종 점수 반환

# 전체 게임 진행 함수
field = [list(input()) for _ in range(rows)]
answer = 0
while True:
    prev_field = [row[:] for row in field]      # 이전 필드 상태 저장
    score = play_puyo(field)                    # 한 번의 게임 진행
    answer += score                             # 점수 누적
    # 더 이상 제거할 뿌요가 없고, 필드 상태가 변하지 않았다면 종료
    if score == 0 and prev_field == field:
        break

print(answer)