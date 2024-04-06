import sys
from collections import Counter
input = sys.stdin.readline

# 숫자의 개수 n을 입력받음
n = int(input())

# 숫자 리스트를 입력받고 정렬
numList = [int(input()) for _ in range(n)]
numList.sort()

# 산술평균을 구함
average = round(sum(numList) / n)

# 중앙값을 구함
median = numList[n//2]

# 숫자 리스트에서 각 숫자의 개수를 세고, 가장 많이 나오는 두 숫자를 찾아 배열로 반환 (ex : [(1, 3), (2, 2)] )
counterList = Counter(numList).most_common(2)

# 최빈값을 구함
if len(counterList) == 1:                       # 숫자 리스트 배열의 개수가 1개면 그 숫자 반환
    frequent = counterList[0][0]
elif counterList[0][1] == counterList[1][1]:    # 개수가 가장 많이 나오는 두 숫자의 개수가 같으면 두번째로 작은 수 반환
    frequent = counterList[1][0]
else:                                           # 개수가 가장 많이 나온 수 반환
    frequent = counterList[0][0]
    
# 범위를 구함
scope = numList[-1] - numList[0]

# 결과를 출력
print(average, median, frequent, scope, sep='\n')