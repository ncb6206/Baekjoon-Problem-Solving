stack = []          # 뽑은 인형을 쌓는 바구니 스택
boardcopy = []      # 원본 보드 복사본
count = 0           # 터트려서 사라진 인형의 개수

# 보드에서 인형 뽑기를 하는 함수
def pick(board, idx):
    global count
    for i in range(len(board)):
        # 해당 열에서 첫번째로 만난 인형을 찾음
        if board[i][idx] != 0:
            temp = board[i][idx]    # 인형 값 임시 저장           
            board[i][idx] = 0       # 해당 위치의 인형 제거
            
            # 스택에 인형이 있는 경우
            if stack:
                # 스택 맨 위의 인형과 현재 인형이 같은 경우
                if stack[-1] == temp:
                    stack.pop()     # 스택의 맨 위의 인형 제거
                    count += 2      # 터트린 인형의 개수 2 증가
                # 스택 맨 위의 인형과 현재 인형이 다르면 스택에 현재 인형 추가
                else:
                    stack.append(temp)  
            # 스택이 비어 있는 경우 스택에 현재 인형 추가
            else:
                stack.append(temp)
            return

def solution(board, moves):
    boardcopy = board[:]    # 원본 보드 복사
    
    for idx in moves:
        # moves 순서대로 인덱스의 인형 뽑기
        pick(boardcopy,idx-1)

    return count