# 직접 푼 알고리즘
A,B = input().split()
reverseA, reverseB = '',''
for i in range(len(A)-1,-1,-1):
    reverseA += A[i]
for i in range(len(B)-1,-1,-1):
    reverseB += B[i]

if(int(reverseA) > int(reverseB)):
    print(reverseA)
else:
    print(reverseB)

# 인터넷에서 검색한 알고리즘
'''
num1, num2 = input().split()
num1 = int(num1[::-1])  # [::-1] : 역순
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else :
    print(num2)
'''