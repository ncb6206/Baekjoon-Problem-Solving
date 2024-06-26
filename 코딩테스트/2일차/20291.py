import sys

N = int(sys.stdin.readline())
fileCount = {}

for _ in range(N):
    name, extend = map(str,sys.stdin.readline().split('.'))
    fileCount[extend.rstrip()] = fileCount.get(extend.rstrip(),0) + 1

for i in sorted(fileCount.items()):
    print(*i)