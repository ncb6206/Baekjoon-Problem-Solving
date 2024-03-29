import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
arrayN = list(map(int,input().split()))
M = int(input())
arrayM = list(map(int,input().split()))
countDict = defaultdict(int)

for i in arrayN:
    countDict[i] += 1

print(' '.join(str(countDict[j]) for j in arrayM))
