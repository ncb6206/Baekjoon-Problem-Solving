import sys

A, B = map(str,sys.stdin.readline().split())
backA,backB = int(A[::-1]),int(B[::-1])

print(max(backA,backB))