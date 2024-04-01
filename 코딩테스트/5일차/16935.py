import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())

nemo = [list(input().split()) for _ in range(N)]
way = int(input())

if way == 1:
    result = [[0]*M for _ in range (N)]
    for i in range(N):
        for j in range(M):
            result[i][j] = nemo[N-1-i][j]
elif way == 2:
    result = [[0]*M for _ in range (N)]
    for i in range(N):
        for j in range(M):
            result[i][j] = nemo[i][M-1-j]
elif way == 3:
    result = [[0]*N for _ in range (M)]
    for i in range(N):
        for j in range(M):
            result[j][N-1-i] = nemo[i][j]
elif way == 4:
    result = [[0]*N for _ in range (M)]
    for i in range(N):
        for j in range(M):
            result[M-1-j][i] = nemo[i][j]

for list in result:
    print(*list)