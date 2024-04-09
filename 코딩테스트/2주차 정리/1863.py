import sys
input = sys.stdin.readline

n = int(input())
skyline = []

for _ in range(n):
    skyline.append(list(map(int,input().split())))
    
print(skyline)