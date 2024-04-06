import sys
input = sys.stdin.readline

x,y = map(int,input().split())

left = 1
right = 10 ** 9 + x
winning = y//x * 100

# while left <= right:
#     mid = ( left + right ) // 2
    
print(winning)