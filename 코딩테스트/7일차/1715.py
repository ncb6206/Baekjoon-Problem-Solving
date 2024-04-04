# 1시간동안 고민하다가 결국 답을 봐버린 문제 33번째 줄 하나로 해결 가능....

import sys
from heapq import *
input = sys.stdin.readline

# 카드의 개수 n을 입력
n = int(input())

# 카드를 담을 리스트 초기화
card = []

# 비교해야되는 경우의 수 초기화
total = 0

# 카드에 적힌 수를 입력받아 최소 힙에 삽입
for _ in range(n):    
    heappush(card,int(input().rstrip()))
    
# 카드의 개수를 저장
cardLength = len(card)

# 카드 힙 리스트의 길이가 1이 될 때까지 반복
while len(card) > 1:
    # 가장 작은 두 카드를 꺼내고 합친 값을 계산
    first = heappop(card)
    second = heappop(card)
    first_plus_second = first + second
    
     # 합친 값의 합을 total에 더해서 모든 경우의 수 저장
    total += first_plus_second
    # 합친 값을 다시 카드 힙 리스트에 넣음(이렇게 하면 카드 더미가 작은 것부터 먼저 계산되서 최소의 경우의 수가 나오게 됨)
    heappush(card,first_plus_second)    # 그냥 이 코드 한줄로 알고리즘 끝  

# 카드의 총 비용을 출력
# card의 개수가 처음부터 1개면 비교안해도 되니까 0 출력
print(total)