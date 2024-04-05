# 정답 안보고 풀긴 했는데 이건 좀 가라로 한듯;;

import sys
input = sys.stdin.readline

# 좌표 개수 입력 받음
n = int(input())

# 수직선 위에 있는 좌표의 인덱스와 값을 리스트로 생성
x = list(enumerate(map(int,input().split())))

# 값을 기준으로 x 리스트를 정렬
x.sort(key = lambda x: x[1])

# 좌표 압축한 결과 리스트를 초기화
result = [0] * n

# 서로 다른 좌표 X의 개수를 세기 위한 변수 초기화
count = 0

# 0번째 인덱스는 가장 작은 수일테니 1부터 x리스트 개수까지 반복:
for i in range(1,len(x)):
    # 현재 x의 값이 이전 x의 값과 다르면 중복되지 않는 숫자이므로 카운트를 증가시키고 result 리스트에 현재 x의 인덱스 위치로 저장
    if x[i][1] != x[i-1][1]:
        count += 1
        result[x[i][0]] = count
    # 현재 x의 값이 이전 x의 값과 같으면 카운트를 증가시키지 않고 result 리스트에 현재 x의 인덱스 위치로 저장
    else:
        result[x[i][0]] = count

print(*result)

# 이게 정석 답인듯 
# x = list(map(int,input().split()))
# dict = {}
# result = []

# setX = list(set(x))
# setX.sort()

# for i in range(len(setX)):
#     dict[setX[i]] = i

# for j in x:
#     result.append(dict[j])

# print(*result)