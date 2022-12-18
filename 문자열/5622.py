# 직접 짠 알고리즘
N = input()
hap = 0

for i in N:
    if(i=='A' or i=='B' or i=='C'):
        hap += 3
    elif(i=='D' or i=='E' or i=='F'):
        hap += 4
    elif(i=='G' or i=='H' or i=='I'):
        hap += 5
    elif (i == 'J' or i == 'K' or i == 'L'):
        hap += 6
    elif (i == 'M' or i == 'N' or i == 'O'):
        hap += 7
    elif (i == 'P' or i == 'Q' or i == 'R' or i=='S'):
        hap += 8
    elif (i == 'T' or i == 'U' or i == 'V'):
        hap += 9
    elif (i == 'W' or i == 'X' or i == 'Y' or i=='Z'):
        hap += 10

print(hap)

#인터넷 참고한 알고리즘
'''
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)

'''