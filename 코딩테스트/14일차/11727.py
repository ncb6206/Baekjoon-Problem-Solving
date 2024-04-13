import sys
input = sys.stdin.readline

N = int(input())        # N을 입력받음

# N+1 크기의 리스트를 생성하고, 모든 값을 0으로 초기화
# dist[i]는 2xi 크기의 직사각형을 1x2, 2x1, 2x2 타일로 채우는 방법의 수
dist = [0] * (N+1)

 # 2xN 직사각형을 채우는 방법의 수를 계산하는 함수
def pibo(idx):
    # 1부터 idx까지 반복
    for i in range(1,idx+1):
        # 2x1 직사각형일 때, 2x1 타일 하나로 2x1 직사각형을 채울 수 있는 방법은 1가지
        if i == 1:
            dist[i] = 1
        # 2x2 직사각형일 때, 1x2 타일 두 개 또는 2x1 타일 두 개, 2x2 타일 1 개로 채울 수 있는 방법은 3가지
        elif i == 2:
            dist[i] = 3
        # 그 외에 경우, 점화식: dist[i] = dist[i-1] + 2 * dist[i-2]
        else:
            dist[i] = dist[i-1] + dist[i-2] * 2

# N번째 항까지 방법의 수 계산
pibo(N)

# 최종 결과를 10007로 나눈 나머지 출력
print(dist[N]%10007)
