import sys
input = sys.stdin.readline

# 사람의 수 n을 입력받음
n = int(input())

# 각 사람이 돈을 인출하는데 걸리는 시간을 리스트로 입력 받음
p = list(map(int,input().split()))

# 소요 시간이 작은 순서대로 일을 처리하기 위해 오름차순 정렬
p.sort()

time = 0        # 현재 사람이 돈을 인출하는데 걸린 시간
result = 0      # 각 사람이 돈을 인출하는데 걸린 시간을 모두 더한 누적값

# 각 사람마다 반복
for i in p:
    time += i       # 현재 사람이 돈을 인출하는데 걸린 시간
    result += time  # 각 사람이 돈을 인출하는데 걸린 시간을 모두 더한 값

print(result)