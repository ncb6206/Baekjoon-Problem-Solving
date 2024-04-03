import sys
from collections import deque
input = sys.stdin.readline

# 풍선의 개수 n을 입력
n = int(input())

# 풍선의 인덱스와 숫자를 덱으로 생성합니다.
balloon = deque(enumerate(map(int, input().split()), start=1))

# 풍선이 터지는 인덱스를 저장할 리스트
result = []

# 풍선을 모두 터뜨릴 때까지 반복
while balloon:
    # 가장 앞에 있는 풍선을 꺼냄
    temp = balloon.popleft()
    # 풍선의 인덱스를 결과 리스트에 추가
    result.append(temp[0])
    # 풍선을 이동시킬 칸 수를 가져옴
    move = temp[1]
    
    # 이동할 칸 수에 따라 풍선을 이동시킴
    if move > 0:
        balloon.rotate(-(move - 1))  # 오른쪽으로 이동
    elif move < 0:
        balloon.rotate(abs(move))  # 왼쪽으로 이동

# 결과 리스트를 공백을 기준으로 출력
print(*result)