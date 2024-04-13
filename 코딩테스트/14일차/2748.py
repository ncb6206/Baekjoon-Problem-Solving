import sys
input = sys.stdin.readline

N = int(input())    # N을 입력받음
dist = [0] * (N+1)  # N+1 크기의 리스트를 생성하고, 모든 값을 0으로 초기화

# 피보나치 수열의 idx번째 항을 계산하는 함수
def pibo(idx):
    # idx 크기 만큼 반복
    for i in range(idx):
        # i가 0 또는 1이면 dist[i]를 i으로 설정
        if i <= 1:
            dist[i] = i
        # 그 외에 경우, 피보나치 수열의 점화식을 이용하여 dist[i] 계산
        else:
            dist[i] = dist[i-1] + dist[i-2]

# N+1번째 항까지 피보나치 수열을 계산
pibo(N+1)

# 피보나치 수열의 N번째 항 출력
print(dist[N])