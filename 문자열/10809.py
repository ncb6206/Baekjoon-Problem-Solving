#코드는 작성했지만 런타임 에러 뜸
'''
S = list(input())
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','s','y','z']
array = ['-1' for i in range(26)]
number = 0

for a in S:
    i = alphabet.index(a)

    if(array[i]=='-1'):
        array[i]=str(number)

    number += 1

for i in range(26):
    print(array[i])
'''

# 정답 알고리즘
word = input()
alphabet = list(range(97,123))

for x in alphabet:
    print(word.find(chr(x)))
