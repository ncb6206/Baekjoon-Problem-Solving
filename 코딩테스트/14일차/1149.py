import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]
INF = float('inf')
dp = [INF] * N

for i in range(N):
    dp[i] = min(house[i])
    

print(dp)