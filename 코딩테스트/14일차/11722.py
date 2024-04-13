# 그냥 문제가 이해가 안감. 그래서 정답을 봤는데 앞의 수가 다음 수보다 크다면 문제의 조건을 만족한다고 한다
# 각 인덱스에 대해 자신보다 인덱스가 작은 값을 검색하여 조건을 만족하는 수의 개수를 찾는다 

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i],dp[j]+1)
    print(dp)

print(max(dp))