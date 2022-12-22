# 직접 짠 알고리즘
N = input()
croatia = ['c=','c-','d-','lj','nj','s=','z=']
i = 0
hap = 0

while(i<len(N)):
    if(i+1<len(N)):
        if(N[i:i+2] in croatia):
            hap += 1
            i += 2
        elif(i+2<len(N) and N[i:i+3] == 'dz='):
            hap += 1
            i += 3
        else:
            hap += 1
            i += 1
    else:
        hap += 1
        i += 1

print(hap)

# 인터넷 참고한 알고리즘
'''
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))
'''