import sys
from collections import deque
input = sys.stdin.readline

a = int(input())
nge = list(map(int,input().rstrip().split()))

stack = []
result = []
i = 0
imsi = 0
count = 0

for i in range(len(nge)):
    if i == 0:
        imsi = nge[i]
    else:        
        if imsi >= nge[i]:
            stack.append(nge[i])
        else:
            count += 1
            stack.append(imsi)
            imsi = nge[i]
            while stack:
                result.append(imsi)
                stack.pop()

while stack:
    temp = stack[0]
    tempStack = []
    for i in range(1,len(stack)):
        if temp >= stack[i]:
            tempStack.append()
    
    

if count == 0:
    result.append(-1)
    
if stack:
    temp = stack.pop()
    while stack:
        stack.pop()
        result.append(temp)
    result.append(-1)
else:
    result.append(-1)
                
print(*result)