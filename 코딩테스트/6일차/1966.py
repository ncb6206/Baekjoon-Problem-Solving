import sys
from collections import deque
input = sys.stdin.readline

# 테스트 케이스의 개수를 입력
t = int(input())
result = []

# 각 테스트 케이스에 대해 반복
for _ in range(t):
    # 문서의 개수 n과 궁금한 문서의 인덱스 m을 입력
    n, m = map(int, input().rstrip().split())
    # 문서의 중요도를 덱에 입력
    importance = deque(map(int, input().rstrip().split()))

    # 궁금한 문서가 출력될 때까지 반복
    while m >= 0:
        m -= 1
        # 가장 앞에 있는 문서를 꺼냄
        temp = importance.popleft()
        # 꺼낸 문서보다 중요도가 높은 문서가 있는지 확인
        for i in importance:
            if temp < i:
                # 꺼낸 문서보다 중요도가 높은 문서가 있으면 다시 뒤로 넣음
                importance.append(temp)
                # 다시 뒤로 넣었으므로 인덱스 m값을 배열의 끝 인덱스 값으로 조정
                if m < 0:
                    m = len(importance) - 1
                break

    # 궁금한 문서가 몇번째로 인쇄되는지에 대한 순서를 결과 리스트에 저장
    result.append(n - len(importance))

# 각 테스트 케이스에 대한 결과를 출력합니다.
for i in result:
    print(i)