import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int,input().split()))for _ in range(N)]
minVal = float('inf')
visited = [False] * N

def backtracking(start,end,hap):    
    global minVal
    allCheck = True
    for i in range(N):
        if not visited[i]:
            allCheck = False
            visited[i] = True
            if W[start][i] == 0:
                visited[i] = False
                continue
            hap += W[start][i]
            print(f"start:{start}, end:{i}, hap={hap}")
            backtracking(i,end,hap)
            hap -= W[start][i]
            visited[i] = False
    if allCheck and W[start][end] != 0:
        hap += W[start][end]
        print(f"start:{start}, end:{end}, hap={hap}")
        minVal = min(minVal,hap)    
    print('--------------------------')

for i in range(N):
    visited[i] = True
    print(f"Start:{i}")
    backtracking(i,i,0)
    visited[i] = False

print(minVal)

# python으로 풀었을 때 시간 초과가 떴지만 pypy로 풀었을 때는 맞았다고 뜸
# 그치만 N이 최대가 10이어서 permutations를 사용할 수 있었지 그 이상이면 사용하면 안될 듯
# from itertools import permutations
# island = [i for i in range(N)]

# for road in list(permutations(island,N)):
#     hap = 0
#     impossible = False
#     for idx in range(N):
#         if idx == N-1:
#             i,j = road[-1],road[0]
#         else:
#             i,j = road[idx:idx+2]
            
#         if W[i][j] == 0:
#             impossible =True
#             break        
        
#         hap += W[i][j]
        
#         if hap > minVal:
#             impossible =True
#             break
        
#     if not impossible:
#         minVal = min(minVal,hap)

# print(minVal)