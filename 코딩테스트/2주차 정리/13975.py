# 최소힙을 사용해서 문제 풀이 그런데 시간이 5096ms가 나옴. 
# 원래 이런 것인지 더 좋은 알고리즘이 있는 것인지 모르겠음

import sys
from heapq import *
input = sys.stdin.readline

T = int(input())        # 테스트 케이스 수
result = []             # 모든 장을 합치는데 필요한 최소비용의 결과를 저장할 리스트

for _ in range(T):
    total = 0           # 모든 장을 합치는데 필요한 총 비용 초기화
    K = int(input())    # 카드 묶음의 개수 입력
    card = list(map(int,input().split()))   # 각 카드 묶음의 크기를 card 배열에 입력
    heapify(card)       # 최소 힙 생성
    
    # 최소 비용이 나올때까지 힙에서 가장 작은 두 개의 카드 묶음을 꺼내어 병합
    while len(card) > 1:
        x = heappop(card)
        y = heappop(card)
        hap = x + y
        total += hap        # 모든 장을 합치는데 필요한 총 비용에 더함        
        heappush(card,hap)  # 병합한 카드 묶음을 다시 힙에 넣기

    result.append(total)    # 각 테스트 케이스의 모든 장을 합치는데 필요한 최소비용을 결과 리스트에 추가
    
for i in result:
    print(i)