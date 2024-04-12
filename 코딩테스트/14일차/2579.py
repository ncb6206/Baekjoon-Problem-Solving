# 정답을 봤던 문제 else부분의 알고리즘이 중요하다
# n-1번째 계단으로 오는 경우, 마지막 계단 + 마지막 전 계단 + dp[n-3]
# n-2번째 계단으로 오는 경우, 마지막 계단 + dp[n-2]
# 참고 블로그 : https://v3.leedo.me/devs/64

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)
stair = [0]
for _ in range(N):
    stair.append(int(input()))
    
for i in range(1,N+1):
    if i == 1:
        dp[i] = stair[i]
    elif i == 2:
        dp[i] = stair[i] + stair[i-1]
    elif i == 3:
        dp[i] = stair[i] + max(stair[i-1],stair[i-2])
    else:
        dp[i] = max(stair[i] + stair[i-1] + dp[i-3], stair[i] + dp[i-2])
    
print(dp[N])