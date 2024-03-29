import sys
input = sys.stdin.readline

N,M = map(int,input().split())
array = sorted(list(map(int,input().split())))
visited = [False] * N
answer = []
answers = []

def back_tracking(index,n,m):
    if index == m:
        answers.append(' '.join(map(str,answer)))
        return
    # remember는 각 자리 수를 기준으로 초기화 되서 9 9 같은 것도 된다
    remember = 0
    for i in range(n):
        if not visited[i] and remember != array[i]:
            visited[i] = True
            answer.append(array[i])
            remember = array[i]
            back_tracking(index+1,n,m)
            visited[i] = False
            answer.pop()

back_tracking(0,N,M)

print('\n'.join(answers))