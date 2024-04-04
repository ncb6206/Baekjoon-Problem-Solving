# 처음 문제를 봤을 때 잘 이해가 되지 않았지만 다시 확인해보니 
# 카드 묶음을 최소 힙 자료구조로 구성하고
# 카드 힙에서 가장 작은 2개의 카드를 꺼내 더한 뒤 계산된 값을 
# 꺼낸 숫자만큼 다시 카드 힙에 넣어주는 것을 m번 반복하여 
# 최종적으로 카드 힙에 남아있는 모든 수의 합을 계산하여 결과를 반환해주는 알고리즘으로 풀음

import sys
from heapq import *
input = sys.stdin.readline

# 카드의 개수 n과 반복할 횟수 m을 입력
n, m = map(int,input().rstrip().split())

# 합체할 카드를 담을 heap 리스트 초기화
card = []

# 카드를 최소 힙에 삽입
for a in list(map(int,input().rstrip().split())):
    heappush(card,a)

# m번 반복하며 카드 합치기 연산 수행
for _ in range(m):
    # 힙에서 가장 작은 두 수를 꺼내서 합침
    x = heappop(card)
    y = heappop(card)
    summary = x + y
     # 합친 결과를 다시 힙에 넣어 덮어줌
    for _ in range(2):
        heappush(card,summary)

# 카드 힙에 남은 숫자들의 합하여 가장 작은 점수 계산
print(sum(card))