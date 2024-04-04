# 처음에 배열 전체를 전부 다 heapq에 넣었더니 메모리 초과 발생
# 질문 게시판에서 힌트를 얻어 heapq의 크기를 n으로 제한하는 방식을 사용
# heapq의 길이가 n을 초과하면, 가장 작은 값을 pop하여 길이를 n으로 유지
# 이렇게 하면 heapq에는 항상 가장 큰 n개의 값만 남게 됨
# 모든 값을 처리한 후, heapq에는 입력 배열에서 가장 큰 n개의 값이 남음
# 이 heapq에서 heappop 연산을 수행하면, n번째 큰수를 출력할 수 있음

import sys
from heapq import *
input = sys.stdin.readline

# 배열의 크기 n 입력 받기
n = int(input())

# 최소 힙을 구성할 리스트 초기화
heap = []


# n번 반복하여 입력을 받고 최소 힙을 구성
for _ in range(n):
    # 입력된 숫자들을 리스트로 변환하여 최소 힙에 삽입
    for i in list(map(int,input().rstrip().split())):        
        heappush(heap,i)
        # 힙의 크기가 n보다 크다면 가장 작은 값을 힙에서 제거
        if len(heap) > n:
            heappop(heap)

# 최종적으로 heap에 남아있는 값은 입력 배열에서 가장 큰 n개의 값
# 따라서 heap에서 pop하면 가장 큰 n개의 값중 가장 작은값부터 꺼내올 수 있음
print(heappop(heap))