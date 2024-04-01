import sys
input = sys.stdin.readline

N,M = map(int,input().split())

chess = [list(input().rstrip()) for _ in range(N)]

print(N,M,chess)