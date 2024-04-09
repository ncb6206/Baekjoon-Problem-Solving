import sys
input = sys.stdin.readline

n = int(input())
skyline = []
stack = []
count = 0

for _ in range(n):
    x,y = map(int,input().split())
    if not stack:
        stack.append(y)
        count += 1
    elif y > 0:
        if y > skyline[-1][1]:
            stack.append(y)
            count += 1
        else:
            if y in stack:
                if stack[-1] != y:
                    stack.pop()
            else:
                stack.pop()
                stack.append(y)
                count += 1
    else:
        stack.clear()
    skyline.append([x,y])
    # print(stack,count)
    
print(count)