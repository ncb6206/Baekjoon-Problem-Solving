import sys
input = sys.stdin.readline

N, M = map(int,input().split())
laboratory = [list(map(int,input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

print(laboratory)