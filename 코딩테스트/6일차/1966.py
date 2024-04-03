import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
result = []

for _ in range(t):
    n, m = map(int,input().rstrip().split())
    importance = deque(map(int,input().rstrip().split()))

    while m >= 0:
        m -= 1
        temp = importance.popleft()
        for i in importance:
            if temp < i:
                importance.append(temp)
                if m <0:
                    m = len(importance) - 1
                break
    
    result.append(n-len(importance))
    
for i in result:
    print(i)