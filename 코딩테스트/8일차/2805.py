import sys
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())
tree = list(map(int,input().rstrip().split()))
tree.sort()

left = 1
right = tree[-1]

while left <= right:
    mid = (left + right) // 2
    remain = 0
    for i in tree:
        if i > mid:
            remain += (i-mid)
    if remain >= m:
        left = mid + 1
    else:
        right = mid - 1
    
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