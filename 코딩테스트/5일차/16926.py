import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())

nemo = [list(input().split()) for _ in range(N)]
imsi = [[0]*M for _ in range(N)]


print(nemo,imsi)

