import sys
input = sys.stdin.readline

t = int(input())

def checkPS(string):
    temp = []
    for i in string:
        if i == '(':
            temp.append(i)
        else:
            if len(temp) == 0:
                return False
            temp.pop()
    
    if len(temp) == 0:   
        return True
    else:
        return False
    
array = [list(input().rstrip()) for _ in range(t)]

for test in array:
    if checkPS(test):
        print('YES')
    else:
        print('NO')