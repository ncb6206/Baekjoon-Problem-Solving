import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]

print(house)