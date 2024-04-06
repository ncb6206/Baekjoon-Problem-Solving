import sys
input = sys.stdin.readline

# 초기 게임 횟수와 이긴 게임 수 입력 받음
x,y = map(int,input().split())

# 초기 승률 계산
winning = y * 100 // x 

# 이진 탐색을 위한 초기 left와 right 값 설정
left = 1
right = 10 ** 9

# 승률이 변하지 않으면 -1을 출력 하기 위해 -1로 초기화
result = -1

# 이진 탐색 수행
while left <= right:
    mid = ( left + right ) // 2                 # 중간 값 계산
    diff_winning = (y+mid) * 100 // (x+mid)     # 현재 승률 계산
    
    # 현재 승률이 초기 승률과 다른 경우,결과를 갱신하고 더 작은 중간 값으로 이동하기 위해 right값 변경
    if diff_winning != winning:                 
        result = mid
        right = mid - 1
    # 현재 승률이 초기 승률과 같은 경우, 더 큰 중간 값으로 이동하기 위해 left값 변경
    else:
        left = mid + 1
    
# 최소 몇 판 더해야 하는 지 결과 출력
print(result)