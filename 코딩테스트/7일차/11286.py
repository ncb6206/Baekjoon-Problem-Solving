import sys
from heapq import *
input = sys.stdin.readline

# 입력받을 수의 개수 n 입력 받음
n = int(input())

# 음수를 담을 최소 힙과 양수를 담을 최소 힙 초기화
minusHeap = []
plusHeap = []

# 결과를 저장할 리스트를 초기화
result = []

# n번 반복하여 수를 입력받고 처리
for _ in range(n):
    # 연산에 대한 정보를 나타내는 정수 x 입력
    x = int(input())
    
    # x가 양수일 경우 양수 힙에 추가
    if x > 0:
        heappush(plusHeap,x)
        
    # x가 음수일 경우 음수 힙에 x를 양수로 변경해서 추가
    elif x < 0:
        heappush(minusHeap,-x)
        
    # x가 0일 경우
    else:
        # 음수 힙과 양수 힙에 모두 값이 없으면 0을 결과 리스트에 추가
        if not minusHeap and not plusHeap:
            result.append(0)
            
        # 음수 힙에 값이 있고 양수 힙에는 없으면 음수 힙에서 값을 꺼내 음수로 변환해준 뒤 결과 리스트에 추가
        elif minusHeap and not plusHeap:
            result.append(-heappop(minusHeap))
            
        # 양수 힙에 값이 있고 음수 힙에는 없으면 양수 힙에서 값을 꺼내 결과 리스트에 추가
        elif plusHeap and not minusHeap:
            result.append(heappop(plusHeap))
            
        # 음수 힙과 양수 힙에 모두 값이 있을경우면 
        else:
            # 양수 힙의 가장 작은 값이 음수 힙의 가장 작은 값보다 크거나 같으면 음수 힙에서 값을 꺼내 음수로 변환해준 뒤 결과 리스트에 추가
            if minusHeap[0] <= plusHeap[0]:
                result.append(-heappop(minusHeap))
                
            # 음수 힙의 가장 작은 값이 양수 힙의 가장 작은 값보다 크면 양수 힙에서 값을 꺼내 결과 리스트에 추가                
            else:
                result.append(heappop(plusHeap))            

# 결과 리스트 출력
for i in result:
    print(i)