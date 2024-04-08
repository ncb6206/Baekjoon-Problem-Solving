import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)    # 재귀 깊이 제한을 1,000,000으로 설정

N, M, R = map(int,input().split())  # 정점 개수 N, 간선 개수 M, 시작 정점 R 입력
node = [[] for _ in range(N+1)]     # 그래프를 인접 리스트로 표현

for _ in range(M):
    u, v = map(int,input().split()) # 간선 정보 입력받기
    node[u].append(v)               # u번 정점에 v번 정점 연결
    node[v].append(u)               # v번 정점에 u번 정점 연결
    
visited = [False] * (N+1)           # 각 정점의 방문 여부 저장
order = [0] * (N+1)                 # 각 정점의 방문 순서 저장
count = 0                           # 방문 순서 카운트

def dfs(idx):
    global count                    # 전역변수 count를 처리하기 위한 global 처리
    visited[idx] = True             # 현재 정점 idx 방문 처리
    count += 1                      # 방문 순서 증가
    order[idx] = count              # 현재 정점 idx의 방문 순서 저장
    
    node[idx].sort()                # 인접 정점들을 오름차순 정렬
    for adj in node[idx]:
        if not visited[adj]:        # 아직 방문하지 않은 인접 정점이면
            dfs(adj)                # 재귀적으로 DFS 수행
                
dfs(R)  # 시작 정점 R에서 DFS 탐색 시작

for i in range(1,N+1):
    print(order[i])  # 각 정점의 방문 순서 출력