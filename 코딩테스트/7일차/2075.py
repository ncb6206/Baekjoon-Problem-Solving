import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
maxVal = 0
heap = []

for _ in range(n):
    for i in list(map(int,input().rstrip().split())):
        heappush(heap,-i)

for _ in range(n):
    maxVal = -heappop(heap)

print(maxVal)