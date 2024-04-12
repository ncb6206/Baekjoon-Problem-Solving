# 이건 생각을 다르게 했으면 맞았을 듯
# 인접한 숫자 2개의 차이를 배열로 다시 만들어서 내림차순으로 정리 한 뒤에
# N-K번 해서 인접한 걸 같은 조로 만들어주는 과정을 수행

import sys
input = sys.stdin.readline

N, K = map(int,input().split())             # 학생 수와 그룹의 수 입력받기
height = list(map(int,input().split()))     # 학생들의 키 입력받기

# 인접한 학생들의 키 차이를 저장하는 리스트
diff = []
for i in range(N-1):
    diff.append(height[i+1]-height[i])
    
# 키 차이를 내림차순으로 정렬
diff.sort(reverse=True)

# 큰 키 차이 K-1개를 선택하여 그룹을 나누기
result = []
for _ in range(N - K):
    result.append(diff.pop())

# 선택한 키 차이의 합 출력
print(sum(result))