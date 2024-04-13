import sys
input = sys.stdin.readline

N = int(input())        # N을 입력받음
dist = [0] * (N+1)      # N+1 크기의 리스트를 생성하고, 모든 값을 0으로 초기화

# 1부터 N까지 반복
for i in range(1,N+1):
    # i가 1이나 2면 dist[i]를 i로 설정
    if i <= 2:
        dist[i] = i    
    #  # 점화식을 이용하여 dist[i] 계산
    else:
        dist[i] = dist[i-1] + dist[i-2]

# 피보나치 수열의 N번째 항을 10007로 나눈 나머지 출력
print(dist[N] % 10007)