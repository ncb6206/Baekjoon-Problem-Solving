import sys
input = sys.stdin.readline

string = list(input().rstrip())
boom = list(input().rstrip())
result = []
temp = []
i = 0

while i < len(string):
    if string[i] == boom[0]:
        temp.append(string[i])
        while string[i] in boom:
            if string[i] == boom[-1]:
                if temp[-len(boom):] == boom:
                    for _ in range(len(boom)):
                        temp.pop()            
            i += 1
            # print(temp)
            if i == len(string):
                break
            temp.append(string[i])
        result += temp
        temp = []
    else:
        result.append(string[i])       
    i += 1                
    # print(result)     

if result:
    print(''.join(result))
else:
    print('FRULA')