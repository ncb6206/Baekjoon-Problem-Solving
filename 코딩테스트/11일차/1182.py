import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int,input().split())
Array = list(map(int,input().split()))

# 결과값을 저장할 변수 초기화
count = 0

# 모든 조합에 대해 검사
for i in range(1,N+1):
    # 크기 i의 부분집합 구하기
    for comb in list(combinations(Array,i)):
        # 부분집합의 합이 S와 같다면 count를 1 증가시킴
        if sum(comb) == S:
            count += 1   
        
print(count)
