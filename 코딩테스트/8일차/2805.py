import sys
input = sys.stdin.readline

# 나무의 수 n과 집으로 가져가려고 하는 나무의 길이 m 입력 받음
n, m = map(int,input().rstrip().split())

# 각 나무의 길이를 입력받고 오름차순 정렬
tree = list(map(int,input().rstrip().split()))
tree.sort()

# 이진 탐색을 위한 초기 left와 right 값을 설정 right는 가장 큰 나무의 길이로 설정
left = 1
right = tree[-1]

# 이진 탐색 수행
while left <= right:
    mid = (left + right) // 2    # 절단기 높이 값을 구함
    remain = 0                   # 절단기 높이로 잘랐을 때 남는 나무의 길이를 저장할 변수를 초기화
    for i in tree:
        if i > mid:
            remain += (i-mid)    # 절단기 높이보다 긴 나무들을 잘랐을 때 남는 길이를 더함
    # 집으로 가져가려고 하는 나무의 길이가 m보다 크거나 같을 경우, 더 큰 절단기 높이를 위해 left 값으로 이동            
    if remain >= m:
        left = mid + 1
    # 집으로 가져가려고 하는 나무의 길이가 m보다 작을 경우, 더 작은 절단기 높이를 위해 right 값으로 이동            
    else:
        right = mid - 1
    
# 최적의 절단기 높이 값을 구하고 출력
print(right)

# while left < right:
#     remain = 0
#     height = (left + right) // 2
#     for i in tree:
#         if i > height:
#             remain += (i-height)
#     if remain == m:
#         break
#     elif remain < m:
#         right = height
#     else:
#         left = height
    
# print(height)