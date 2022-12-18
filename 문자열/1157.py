S = input().upper()
array = set(S)
maxcount = 0
alphabet = ''

for i in array:
    if(S.count(i)>maxcount):
        maxcount = S.count(i)
        alphabet = i
    elif(S.count(i)==maxcount):
        alphabet = '?'

print(alphabet)