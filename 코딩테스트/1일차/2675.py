import sys

T = int(sys.stdin.readline())

for _ in range(T):
    R, S = sys.stdin.readline().split()

    for alpha in S:
        for _ in range(int(R)):
            print(alpha, end="")
    print("")