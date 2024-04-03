import sys
from collections import deque
input = sys.stdin.readline

# 탑의 개수 n을 입력받음
n = int(input())

# 각 탑의 높이와 인덱스를 리스트로 생성
top = list(enumerate(map(int,input().split()),start=1))

# 스택을 초기화
stack = []

# 수신 탑의 인덱스를 저장할 리스트를 초기화
result = []

# 각 탑에 대해 반복
for i in range(n):
     # 스택이 비어있지 않고 스택의 탑의 높이가 현재 탑의 높이보다 작을 때까지 반복
    while stack:
        if stack[-1][1] < top[i][1]:
            stack.pop()  # 맨 뒤에 있는 스택을 pop
        else:
            result.append(stack[-1][0])  # 수신 탑의 인덱스를 결과 리스트에 추가
            break
    if not stack:
        result.append(0)  # 스택이 비어있으면 수신 탑이 없으므로 0을 추가
    stack.append(top[i])  # 현재 탑을 스택에 추가

# 결과 리스트를 출력
print(*result)