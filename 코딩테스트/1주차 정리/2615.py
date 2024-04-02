# 풀지는 못했지만 이런 로직으로 푼다~

def main():
    board = [list(map(int, input().split())) for _ in range(19)]
    delta = [(0, 1), (1, 0), (1, 1), (-1, 1)] # 가장 왼쪽 위 오목알을 찾을 것이므로, 이 4가지 방향만 확인하면 돼요.
    for i in range(19):
        for j in range(19):
            if board[i][j] == 0: # 오목알이 아니면 그대로 넘어가요.
                continue
            for dx, dy in delta:
                # 이전 방향에 같은 오목알이 있으면 넘어가요.
                if 0 <= i - dx < 19 and 0 <= j - dy < 19 and board[i - dx][j - dy] == board[i][j]:
                    continue
                nx, ny = i, j
                cnt = 1
                while True:
                    nx, ny = nx + dx, ny + dy
                    # 범위를 벗어나거나, 시작한 오목알과 다른 오목알이 나오면 break
                    if nx < 0 or nx >= 19 or ny < 0 or ny >= 19 or board[nx][ny] != board[i][j]:
                        break
                    cnt += 1
                
                # 오목이 완성되었으면 출력하고 종료해요.
                if cnt == 5:
                    print(board[i][j])
                    print(i + 1, j + 1)
                    return
    # 모두 탐색했는데 오목이 없으면 0을 출력해요.
    print(0)
    return


if __name__ == "__main__":
    main()
