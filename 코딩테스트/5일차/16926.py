import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())

nemo = [list(input().split()) for _ in range(N)]
imsi = [[0]*M for _ in range(N)]


# for i in range(N):
#     for j in range(M):
#         imsi[i][j] = 

print(nemo,imsi)

