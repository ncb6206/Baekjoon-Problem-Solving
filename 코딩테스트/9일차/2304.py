# 전체 넓이를 구해서 지붕이 설치 안된 나머지 부분의 넓이를 뺀 값을 구하려고 했지만 실패

import sys
input = sys.stdin.readline

# 막대 기둥 개수 n을 입력받음
n = int(input())

# 각 직사각형의 왼쪽 아래 모서리 좌표와 높이를 입력 받고 왼쪽 아래 모서리 좌표를 기준으로 정렬
square = [tuple(map(int,input().split())) for _ in range(n)]
square.sort()

# 가장 높은 직사각형의 높이와 인덱스를 초기화
maxHeight = 0
maxIdx = 0
area = 0

# 가장 높은 직사각형의 높이와 인덱스를 찾음
for i in range(n):
    if maxHeight <= square[i][1]:
        maxHeight = square[i][1]
        maxIdx = i


# 왼쪽에서부터 가장 높은 직사각형까지의 넓이를 계산
currentHeight = 0
for j in range(0,maxIdx):
    currentHeight = max(currentHeight,square[j][1])
    area += (square[j+1][0] - square[j][0]) * currentHeight
    
# 오른쪽에서부터 가장 높은 직사각형까지의 넓이를 계산
currentHeight = 0
for j in range(n-1,maxIdx,-1):
    currentHeight = max(currentHeight,square[j][1])
    area += (square[j][0] - square[j-1][0]) * currentHeight
    
# 가장 높은 직사각형의 넓이를 추가
area += maxHeight

# 결과를 출력
print(area)