import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
balloon = deque(map(int,input().split()))
cache = balloon
count = 1
result = []

for _ in range(n):
    move = cache.popleft()
    cache.appendleft(0)
    result.append(count)
    print('0돌리기 전')
    print(cache)
    print(move,count)
    while cache[0] == 0:
        temp = cache.popleft()
        cache.append(temp)
        move -= 1
        count += 1
        if count == n+1:
            count = 1
    
    print('0돌리기 후')
    print(cache)
    print(move,count)
                
    while move != 0:
        if move > 0:
            temp = cache.popleft()
            if(temp != 0):
                move -= 1
            cache.append(temp)
            count += 1
            if count == n+1:
                count = 1
        elif move < 0:
            temp = cache.pop()
            if(temp != 0):
                move += 1
            cache.appendleft(temp)
            count -= 1
            if count == 0:
                count = n

        print(cache)
        print(move,count)
    print('---------------------')

print(result)