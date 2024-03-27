import sys

line = 1
X = int(sys.stdin.readline())

while X > line :
    X -= line
    line += 1

if line % 2 == 0:
    print(f"{X}/{line-X+1}")
else:
    print(f"{line-X+1}/{X}")

