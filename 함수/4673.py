# 답 확인하기전 짠 알고리즘
def d(n):
    hap = 0
    number = 0
    for i in str(n):
        number += int(i)
    hap += n+number
    return hap

array = list()
selfnumber = [i for i in range(1,10001)]
num = 1

while True:
    if(num>10000):
        break

    if(selfnumber.count(d(num))==1):
        selfnumber.pop(selfnumber.index(d(num)))

    num += 1

for i in selfnumber:
    print(i)
    
# 답 확인하고 난 후 알고리즘
'''
#set을 사용하는 이유는 list와 set 둘다 배열을 만들수 있지만 set은 중복값 포함 안함
array = set(range(1,10001))
gennumber = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    gennumber.add(i)

selfnumber = sorted(array-gennumber)
for i in selfnumber:
    print(i)
'''