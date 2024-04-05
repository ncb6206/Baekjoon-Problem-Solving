# 문제 이해조차 안되었는데 답을 보고 나니까 문제 이해가 되었음
# 처음에 left = home[0], right = home[-1] 이렇게 초기화하였는데
# 거리의 최대값을 구하는 거여서 나올 수 있는 최소거리인 1을 left에 home 리스트 끝에서 처음 값을 뺀걸 최대거리로 하여서 right에 넣음

import sys
input = sys.stdin.readline

n, c = map(int,input().split())
home = []

for _ in range(n):
    home.append(int(input().rstrip()))
home.sort()
    
left = 1    # 공유기 거리 최소
right = home[-1] - home[0]  # 공유기 거리 최대
result = 0

# 재귀로 적절한 두 공유기 사이의 거리를 찾음
while left <= right:
    mid = (left+right) // 2     # 현재 공유기 거리
    current = home[0]
    count = 1
    
    # 현재 공유기 거리로 모든 집에서 와이파이를 사용하려면 공유기가 몇 대 필요한 지 체크
    for i in range(len(home)):
        if home[i] >= current + mid:
            count += 1
            current = home[i]
    # print(mid,count,current,left,right)
    # 공유기 설치 수가 목표 보다 크거나 같으면 공유기 사이 거리 늘림
    if count >= c:
        result = mid
        left = mid + 1
    # 공유기 설치 수가 목표 보다 작으면 공유기 사이 거리 줄임
    else:
        right = mid - 1
    
print(result)
