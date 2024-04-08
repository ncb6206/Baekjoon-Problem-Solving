import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
queue=deque()
count = 0

computer = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    computer[a].append(b)
    computer[b].append(a)
    
def bfs(idx):
    global count
    queue.append(computer[idx])
    visited[idx] = True
    while queue:
        current = queue.popleft()
        for adj in current:
            if not visited[adj]:
                count += 1
                queue.append(computer[adj])
                visited[adj] = True    
    
bfs(1)   
    
print(count)