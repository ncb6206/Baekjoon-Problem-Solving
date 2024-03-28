import sys

word = sys.stdin.readline().rstrip().upper()
wordSet = set(word)
mostUse = ""
mostCount = 0

for i in wordSet:
    if mostCount < word.count(i):
        mostUse = i
        mostCount = word.count(i)
    elif mostCount == word.count(i):
        mostUse = "?"

print(mostUse)