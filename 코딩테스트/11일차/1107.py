import sys
input = sys.stdin.readline

N = int(input())    # 이동하려는 채널
M = int(input())    # 고장난 버튼의 개수

# 고장난 버튼 입력받기
if M != 0:
    broken = list(input().rstrip().split())
else:
    broken = []

# 최소 횟수 초기화
minCount = abs(100 - N)      # 채널 100번에서 이동하는 횟수가 최소 횟수의 초기값

# 모든 채널에 대해 검사
for i in range(10 ** 6 + 1):
    breakNum = False         # 현재 채널의 숫자가 고장난 버튼을 포함하는지 확인하는 변수
    
    # 현재 채널의 각 숫자가 고장난 버튼인지 확인
    for j in str(i):
        if j in broken:
            breakNum = True
            break
    
    # 현재 채널의 숫자가 고장난 버튼을 포함하지 않는 경우
    if not breakNum:
        # 현재 채널과 이동하려는 채널의 차이 절댓값 계산
        absNum = abs(N-i)
        # 현재 최소 횟수와 현재 채널로 이동하는 데 필요한 횟수 중 작은 값으로 최소 횟수 갱신
        minCount = min(minCount,absNum+len(str(i)))
    
print(minCount)    

# 시도했었던 코드(정말 말이 안되게 길게 짰고 결국엔 답도 못맞춤)
# N = int(input())
# strN = str(N)
# M = int(input())
# startChannel = 100
# remote = [i for i in range(10)]
# if M != 0:
#     broken = list(map(int,input().split()))
# else:
#     broken = []
# button = list(set(remote) - set(broken))
# result = []
# computable = []
# minClick = float('inf')

# if N == startChannel:
#     print(0)
#     exit(0)    

# for i in range(len(strN)):
#     minVal = float('inf')
#     intNum = int(strN[:i+1])
#     stack = []
#     for i in button:
#         if abs(intNum-i) == minVal:
#             stack.append(i)
#         elif abs(intNum-i) < minVal:
#             minVal = abs(intNum-i)
#             while stack:
#                 stack.pop()
#             stack.append(i)
#         # print(stack,minVal)
#     result.append(stack)            
    
# def calcNum(num,stack):
#     if len(num) == len(strN):
#         return computable.append(int(num))        
#     for i in stack[0]:
#         calcNum(num+str(i),stack[1:])
    
# calcNum('',result)

# for comp in computable:
#     click = len(str(comp)) + abs(N-comp)
#     minClick = min(minClick,click)    
    
# print(result, computable)

# print(min(minClick,abs(startChannel-N)))
