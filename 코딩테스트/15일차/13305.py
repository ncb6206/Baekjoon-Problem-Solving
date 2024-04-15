import sys
input = sys.stdin.readline

N = int(input())                            # 도시의 개수 입력받기
road = list(map(int,input().split()))       # 각 도시 간 거리 입력받기
oil = list(map(int,input().split()))        # 각 도시의 주유소 리터당 가격 입력받기

hap = 0     # 총 비용을 저장할 변수
j = 0       # 현재 주유소의 인덱스
temp = 0    # 최소 주유소 가격의 인덱스를 저장할 변수

# 도시 간 거리만큼 반복
for i in range(len(road)):
    # 첫 번째 도시라면 현재 주유소 가격에 거리를 곱해 비용 누적
    if not hap:
        hap += (oil[j]*road[i])
    # 첫 번째 도시가 아니라면
    else:
        if oil[temp] > oil[j]:  # 현재 주유소 가격이 최소 주유소 가격보다 낮다면 최소 주유소 인덱스 갱신
            temp = j        
        hap += (oil[temp]*road[i])  # 최소 주유소 가격에 거리를 곱해 비용 누적
    j += 1  # 다음 도시로 이동

print(hap)  # 총 비용 출력