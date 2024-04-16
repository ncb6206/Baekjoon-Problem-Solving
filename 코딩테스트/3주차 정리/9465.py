import sys
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    N = int(input())
    dp = [[0]*N for _ in range(2)] 
    visited = [2] * N
    sticker = [list(map(int,input().split())) for _ in range(2)]
    
    for i in range(N):
        if i == 0:
            dp[0][i] = sticker[0][i]
            dp[1][i] = sticker[1][i]
        elif i == 1:
            dp[0][i] = dp[1][i-1] + sticker[0][i]
            dp[1][i] = dp[0][i-1] + sticker[1][i]
        else:
            dp[0][i] = max(dp[1][i-1],dp[1][i-2],dp[0][i-2]) + sticker[0][i]
            dp[1][i] = max(dp[0][i-1],dp[0][i-2],dp[1][i-2]) + sticker[1][i]
        
    result.append(max(dp[0][N-1],dp[1][N-1]))
    
for i in range(T):
    print(result[i])