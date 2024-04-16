import sys
input = sys.stdin.readline

T = int(input())        # 테스트 케이스의 개수 입력받기
result = []             # 각 테스트 케이스의 결과를 저장할 리스트

for _ in range(T):
    N = int(input())    # 스티커의 행 개수 입력받기
    dp = [[0]*N for _ in range(2)]      # 각 행의 최대 점수를 저장할 2차원 리스트
    sticker = [list(map(int,input().split())) for _ in range(2)]    # 스티커의 점수 정보 입력받기
    
    # 각 열을 탐색
    for i in range(N):
        # 첫 번째 열이라면 
        if i == 0:      
            dp[0][i] = sticker[0][i]    # 첫 번째 행의 첫 번째 스티커 선택
            dp[1][i] = sticker[1][i]    # 두 번째 행의 첫 번째 스티커 선택
        # 두 번째 열이라면
        elif i == 1:    
            # 이전 열(첫 번째 열)의 두 번째 행 최대 점수와 첫 번째 행의 두 번째 스티커 점수를 더해서 dp[0][i]에 저장
            dp[0][i] = dp[1][i-1] + sticker[0][i]   
            # 이전 열(첫 번째 열)의 첫 번째 행 최대 점수와 두 번째 행의 두 번째 스티커 점수를 더해서 dp[1][i]에 저장
            dp[1][i] = dp[0][i-1] + sticker[1][i] 
        # 그 외의 열이라면 
        else:     
            # 첫 번째 행의 i번째 스티커 선택
            # 이전 열(i-1번째 열)의 두 번째 행, i-2번째 열의 첫 번째, 두 번째 행 중 최대 점수와 현재 스티커 점수를 더해서 dp[0][i]에 저장      
            dp[0][i] = max(dp[1][i-1],dp[1][i-2],dp[0][i-2]) + sticker[0][i]
            # 두 번째 행의 i번째 스티커 선택
            # 이전 열(i-1번째 열)의 첫 번째 행, i-2번째 열의 첫 번째, 두 번째 행 중 최대 점수와 현재 스티커 점수를 더해서 dp[1][i]에 저장
            dp[1][i] = max(dp[0][i-1],dp[0][i-2],dp[1][i-2]) + sticker[1][i]
        
    result.append(max(dp[0][N-1],dp[1][N-1]))   # 맨 뒤에 열의 두 행 중 최대 점수를 결과 리스트에 추가
    
for i in range(T):
    print(result[i])    # 각 테스트 케이스의 결과 출력