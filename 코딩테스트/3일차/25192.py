import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
chatDict = defaultdict(int)
count = 0

for _ in range(N):
    chat = input().rstrip()
    if(chat == 'ENTER'):
        count += len(chatDict.keys())
        chatDict.clear()
        continue
    chatDict[chat] = 1

count += len(chatDict.keys())
print(count)