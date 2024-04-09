# 인덱스 오류가 자꾸 떠서 확인해봤더니 visited리스트에 범위를 100000으로 설정해서 
# visited[100000]을 방문하였을 때 오류가 발생한 걸 확인하고 수정

import sys
from collections import deque
input = sys.stdin.readline

# 수빈이와 동생이 있는 위치 입력
N, K = map(int,input().split())

# 방문 여부를 저장할 리스트 초기화(여기서  100000+1을 해줘야 오류가 생기지 않음)
visited = [False for _ in range(10 ** 5+1)]

# 너비 우선 탐색을 이용해 N에서 K까지 도달하는 최소 연산 횟수를 구함
def bfs(idx):
    queue = deque()
    queue.append([idx,0])       # 현재 위치와 연산 횟수 큐에 추가
    visited[idx] = True         # 현재 위치 방문 처리
    
    while queue:
        # 큐에서 현재 위치와 연산 횟수 꺼내기
        current,count = queue.popleft()     
        
        # 현재 위치가 동생이 있는 위치와 같다면 연산 횟수 반환
        if current == K:                    
            return count     
           
        # 연산 하기 전 연산 횟수 증가         
        count += 1                          
        
        # 이동할 수 있는 3가지 경우 체크
        for case in range(3):
             # 1. 현재 위치 - 1 을 한 경우
            if case == 0 and 0 <= current - 1 <= 10 ** 5 and not visited[current - 1]:
                # 현재 위치 -1만큼 이동한 위치와 연산 횟수를 큐에 넣음, 현재 위치 - 1만큼 이동한 위치를 방문 처리
                queue.append([current - 1,count])
                visited[current - 1] = True
            # 2. 현재 위치 + 1만큼 이동한 위치와 연산 횟수를 큐에 넣음, 현재 위치 + 1만큼 이동한 위치를 방문 처리
            elif case == 1 and 0 <= current + 1 <= 10 ** 5 and not visited[current + 1]:
                queue.append([current + 1,count])
                visited[current + 1] = True
            # 3. 현재 위치 * 2만큼 이동한 위치와 연산 횟수를 큐에 넣음, 현재 위치 * 2만큼 이동한 위치를 방문 처리
            elif case == 2 and 0 <= current*2 <= 10 ** 5 and not visited[current * 2]:
                queue.append([current * 2,count])
                visited[current * 2] = True

print(bfs(N))