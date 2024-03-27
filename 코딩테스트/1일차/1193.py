import sys

X = int(sys.stdin.readline())

bunza = 1
bunmo = 1
bunzaMinusbunmoPlusCount = 0
bunzaPlusbunmoMinusCount = 0

def bunzaMinusbunmoPlus(x1,x2):
    global bunzaMinusbunmoPlusCount, bunzaPlusbunmoMinusCount
    x2 += 1
    if x1 - 1 > 0:
        x1 -= 1
    else:
        bunzaMinusbunmoPlusCount = 0
        bunzaPlusbunmoMinusCount = 1

    return x1,x2

def bunzaPlusbunmoMinus(x1,x2):
    global bunzaMinusbunmoPlusCount, bunzaPlusbunmoMinusCount
    x1 += 1
    if x2 - 1 > 0:
        x2 -= 1
    else:
        bunzaMinusbunmoPlusCount = 1
        bunzaPlusbunmoMinusCount = 0

    return x1,x2


for i in range(1,X):
    if i == 1:
        bunza, bunmo = bunzaMinusbunmoPlus(bunza, bunmo)

    elif bunzaMinusbunmoPlusCount == 1:
        bunza, bunmo = bunzaMinusbunmoPlus(bunza, bunmo)

    elif bunzaPlusbunmoMinusCount == 1:
        bunza, bunmo = bunzaPlusbunmoMinus(bunza, bunmo)

print(f"{bunza}/{bunmo}")