import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())

nemo = [list(input().split()) for _ in range(N)]

way = int(input())

print(N,M,R,nemo,way)