import sys
input = sys.stdin.readline

# 입국심사대 수 n과 사람 수 m을 입력 받음
n,m = map(int,input().split())

# 각 심사대에서 심사를 하는데 걸리는 시간을 입력 받을 리스트 초기화
entry = []

# 이진 탐색을 위한 초기 left와 right 값을 설정
left = 1
# 여기서 right의 값은 T의 최댓값과 n이 1이고 m이 10 ** 9인 경우에 최악의 수가 되므로 m을 곱한값으로 설정해주어야 모든 경우의 수를 따질 수 있다(이 부분은 정답 참고함)
right = (10 ** 9) * m  

# 심사를 마치는데 걸리는 시간의 최솟값을 저장할 변수 초기화
result = 0

# 각 심사대에서 심사를 하는데 걸리는 시간을 입력 받고 오름차순 정렬
for _ in range(n):
    entry.append(int(input()))
entry.sort()

# 이진 탐색을 수행
while left <= right:
    mid = (left + right) // 2   # 심사를 마치는데 걸리는 시간 값을 구함
    count = 0                   # 심사를 마치는데 걸리는 시간내에 처리할 수 있는 사람의 수를 저장할 변수를 초기화
    for i in entry:
        count += mid // i       # 각 심사대 마다 심사를 마치는데 걸리는 시간 내에 처리할 수 있는 사람의 수를 더함
    # 처리할 수 있는 사람의 수가 m 이상인 경우, 결과를 갱신하고 심사를 마치는데 걸리는 시간이 더 작은 값으로 이동
    if count >= m:              
        result = mid
        right = mid - 1 
    # 처리할 수 있는 사람의 수가 m 미만인 경우, 심사를 마치는데 걸리는 시간 값이 더 큰 값으로 이동
    else:
        left = mid + 1        
    
# 심사를 마치는데 걸리는 시간의 최솟값 출력    
print(result)