import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())
visited = [False for _ in range(10 ** 5+1)]

def bfs(idx):
    queue = deque()
    queue.append([idx,0])
    visited[idx] = True
    while queue:
        current,count = queue.popleft()
        if current == K:
            return count        
        count += 1
        for case in range(3):
            if case == 0 and 0<= current - 1 <= 10 ** 5 and not visited[current - 1]:
                queue.append([current - 1,count])
                visited[current - 1] = True
            elif case == 1 and 0<= current + 1 <= 10 ** 5 and not visited[current + 1]:
                queue.append([current + 1,count])
                visited[current + 1] = True
            elif case == 2 and 0<= current*2 <= 10 ** 5 and not visited[current * 2]:
                queue.append([current * 2,count])
                visited[current * 2] = True

print(bfs(N))