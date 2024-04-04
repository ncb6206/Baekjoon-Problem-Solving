# 처음에 combinations를 사용해서 착용할 수 있는 모든 경우의 수를 구할려고 했는데 
# 메모리 초과가 계속 발생해서 구글링으로 다른 접근 방식을 찾아봄
# 각 옷 종류별로 '착용하지 않는 경우'를 포함하여 +1을 해주고 
# 서로 곱하면 모든 옷 종류의 전체 경우의 수를 알 수 있음
# 그러나 이 전체 경우의 수에 아무 옷도 착용하지 않는 경우가 포함되어 있어
# 최종 결과에서 1을 빼서 이 경우를 제외하여 예외 처리를 함

import sys
from collections import defaultdict
input = sys.stdin.readline

# 테스트 케이스 수 입력받기
t = int(input())

# 각 테스트 케이스에 대한 결과를 저장할 리스트
result = []

# 각 테스트 케이스에 대해 반복
for _ in range(t):
    # 의상 종류별 개수를 저장할 defaultdict
    wear = defaultdict(int)
    
    # 의상 수 입력받기
    n = int(input())
    
    # 각 의상의 이름과 종류 입력받아, 종류별 개수 카운트
    for _ in range(n):
        name, type = map(str,input().rstrip().split())
        wear[type] += 1
        
    # 알몸인 경우 + (의상 종류1 고를 수 있는 경우 * 의상 종류2 고를 수 있는 경우 * ...)
    cnt = 1
    for i in wear.values():
        cnt *= i + 1
    
    # 알몸인 경우 제외
    result.append(cnt-1)
    
# 각 테스트 케이스 결과 출력
for i in result:
    print(i)