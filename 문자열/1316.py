N = int(input())
groupword = 0

for _ in range(N):
    word = input()
    i = 0
    isgroupword = 0

    while(i < len(word)):
        counts = 1
        alp = word.count(word[i])

        while(i+1 < len(word) and word[i] == word[i+1]):
            i += 1
            counts += 1

        i += 1

        if(counts != alp):
            isgroupword += 1
            break

    if(isgroupword == 0):
        groupword += 1

print(groupword)