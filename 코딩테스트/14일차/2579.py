# 정답을 봤던 문제 else부분의 알고리즘이 중요하다
# n-1번째 계단으로 오는 경우, 마지막 계단 + 마지막 전 계단 + dp[n-3]
# n-2번째 계단으로 오는 경우, 마지막 계단 + dp[n-2]
# 참고 블로그 : https://v3.leedo.me/devs/64

import sys
input = sys.stdin.readline

N = int(input())    # 사용자로부터 계단의 개수 N을 입력받음

# N+1 크기의 리스트를 생성하고, 모든 값을 0으로 초기화
# dp[i]는 i번째 계단까지 올라왔을 때의 최대 점수를 저장
dp = [0] * (N+1)

# 계단 점수를 저장할 리스트, 인덱스를 맞추기 위해 0번째 인덱스를 비워둠
stair = [0]

# 사용자로부터 각 계단의 점수를 입력받아 stair 리스트에 저장
for _ in range(N):
    stair.append(int(input()))
    
# 1번째 계단부터 N번째 계단까지 반복
for i in range(1,N+1):
     # 기저 조건 1: 1번째 계단일 때, dp[i]에 stair[i] 저장
    if i == 1:
        dp[i] = stair[i]
    # 기저 조건 2: 2번째 계단일 때, dp[i]에 stair[i] + stair[i-1] 저장
    elif i == 2:
        dp[i] = stair[i] + stair[i-1]
    # 기저 조건 3: 3번째 계단일 때, dp[i]에 stair[i] + max(stair[i-1], stair[i-2]) 저장
    elif i == 3:
        dp[i] = stair[i] + max(stair[i-1],stair[i-2])
    # 그 외에 경우, n-1번째 계단으로 오는 경우, 마지막 계단 + 마지막 전 계단 + dp[n-3]의 값과
    # n-2번째 계단으로 오는 경우, 마지막 계단 + dp[n-2] 중 더 큰값을 dp[i]에 저장
    else:
        dp[i] = max(stair[i] + stair[i-1] + dp[i-3], stair[i] + dp[i-2])

# N번째 계단까지의 최대 점수 출력
print(dp[N])