import sys
input = sys.stdin.readline

N = int(input())        # 센서의 개수
K = int(input())        # 집중국의 개수
sensor = list(map(int,input().split()))     # 센서의 위치 정보 입력받기

# 센서의 개수가 집중국의 개수 이하라면
if N <= K:
    print(0)    # 모든 센서마다 집중국을 배치하면 되므로 최소 거리 합은 0
    exit(0)     # 프로그램 종료

sensor.sort()   # 센서의 위치를 오름차순으로 정렬

diff = []       # 인접한 센서 간의 거리를 저장할 리스트
for i in range(1,N):
    diff.append(sensor[i]-sensor[i-1])       # 센서 간 거리 계산
    
diff.sort()     # 인접한 센서 간의 거리 리스트를 오름차순으로 정렬
result = diff[:(N-K)]   # N-K개의 가장 작은 거리를 선택

print(sum(result))      # 선택된 거리의 합 출력