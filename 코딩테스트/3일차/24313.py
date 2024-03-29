import sys
input = sys.stdin.readline

a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

# a1 <= c 조건 추가하는 건 구글링해서 알게 됨
if a1*n0 + a0 <= c*n0 and a1 <= c:
    print(1)
else:
    print(0)
