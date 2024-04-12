# 정렬하는 거랑 잘 정렬해놓으면 for문을 한번만 돌려도 답이 나온다는 게 포인트

import sys
input = sys.stdin.readline

N = int(input())    # 회의의 개수를 입력받음
meeting = []        # 회의 정보를 담을 리스트 생성

# 회의 정보 입력받아 meeting 리스트에 저장
for _ in range(N):
    start,end = map(int,input().split())
    meeting.append([start,end])

# 종료 시간을 기준으로 오름차순 정렬을 한 다음, 종료 시간이 같으면 시작 시간을 기준으로 오름차순 정렬
meeting.sort(key=lambda x: (x[1],x[0]))

stack = []      # 회의실 사용 정보를 저장할 스택
stack.append([meeting[0][0],meeting[0][1]])     # 첫 번째 회의 정보 스택에 추가

# 두 번째 회의부터 확인
for i in range(1,N):
    start,end = meeting[i]
    # 직전 회의 종료 시간이 현재 회의 시작 시간보다 작거나 같다면 현재 회의 추가
    if stack[-1][1] <= start:
        stack.append([start,end])

# 스택에 저장된 회의 개수 출력
print(len(stack))