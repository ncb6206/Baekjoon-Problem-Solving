import sys
from heapq import *
input = sys.stdin.readline

# 거인의 수 n, 센티의 키 centi, 마법의 뿅망치 횟수 제한 t를 입력 받음
n, centi, t = map(int,input().split())
giant = [-int(input()) for _ in range(n)]  # 거인들의 키를 최소 힙에 추가하기 위해 음수로 변환하여 리스트에 삽입
heapify(giant)  # 거인들의 키 리스트를 힙큐로 변경

count = 0   # 뿅망치가 사용된 횟수를 저장할 변수 초기화
maxHeight = -heappop(giant)     # 힙에서 가장 큰 값(절대값이 가장 작은 값 = 가장 큰 거인의 키)을 꺼냄

# t번의 시뮬레이션을 수행
for _ in range(t):
    # 만약 가장 큰 거인의 키가 1이거나 최소 높이 이하라면 반복문을 종료
    if maxHeight == 1 or maxHeight < centi:
        break
    else:
        # 현재 가장 큰 거인의 키를 절반으로 줄이고 음수로 변환해서 힙에 추가
        heappush(giant, -(maxHeight // 2))
        count += 1                  # 뿅망치가 사용된 횟수 1회 추가
    maxHeight = -heappop(giant)     # 다음 가장 큰 키를 가져옴

# 만약 가장 큰 거인의 키가 센티의 키보다 크거나 같다면 'NO'와 가장 큰 거인의 키를 출력
if maxHeight >= centi:
    print('NO',maxHeight,sep='\n')
# 그렇지 않다면 'YES'와 최소로 뿅망치가 사용된 횟수를 출력
else:
    print('YES',count,sep='\n')