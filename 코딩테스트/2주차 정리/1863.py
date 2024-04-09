import sys
input = sys.stdin.readline

N = int(input())
stack = []
count = 0

# 정답보고 작성한 코드
for _ in range(N):
    x,y = map(int,input().split())
    
    # 스택에 아무것도 없으면 현재 높이를 스택에 추가하고 continue
    if not stack:
        stack.append(y)
        continue

    # 스택이 존재하고 현재 높이가 스택 맨 위의 높이보다 작으면
    while stack and y < stack[-1]:
        # 스택 맨 위의 높이를 제거하고 count 증가
        count += 1
        stack.pop()
        
    # 스택이 비었거나 현재 높이가 스택 맨 위의 높이와 다르면
    if not stack or (stack and y != stack[-1]):
        stack.append(y)

# 스택이 비어있지 않으면
while stack:
    # 스택 맨 위의 높이가 0보다 크면 count 증가 후 제거
    if stack[-1] > 0:
        count += 1
    stack.pop()

print(count)

# 내가 작성했던 코드 틀렸다는 결과가 나옴
# for _ in range(N):
#     x,y = map(int,input().split())
    
#     # 스택이 비어있으면 현재 높이 y를 스택에 추가하고 count를 1 증가
#     if not stack:
#         stack.append(y)
#         count += 1
        
#     # 현재 높이 y가 양수인 경우
#     elif y > 0:
#         # 현재 높이 y가 스택의 최상단 높이보다 큰 경우
#         if y > stack[-1]:
#             stack.append(y)
#             count += 1
#         else:
#             # 현재 높이 y가 스택의 최상단 높이보다 작고 현재 높이 y가 스택에 있으면
#             if y in stack:
#                 # 스택이 존재하고 스택의 최상단 높이가 현재 높이 y랑 다른 동안 스택 pop
#                 while stack and stack[-1] != y:                
#                     stack.pop()
#             # 현재 높이 y가 스택의 최상단 높이보다 작고 현재 높이 y가 스택에 없을 경우
#             else:
#                 # 스택이 존재하고 스택의 최상단 높이가 현재 높이 y보다 작을 동안 스택 pop
#                 while stack and stack[-1] > y:
#                     stack.pop()
#                 # 현재 높이 y를 스택에 추가하고 count를 1 증가
#                 stack.append(y)
#                 count += 1
                
#     # 현재 높이 y가 0인 경우
#     else:
#         # 스택을 모두 비움
#         stack.clear()
    
# print(count)