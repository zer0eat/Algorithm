# 재미있는오셀로게임_4615

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                        # 테스트 케이스
for t in range(T):                                      # 테스트 케이스 반복
    N, M = map(int, input().split())                    # N = 오셀로보드의 크기 / M = 놓을 돌의 수
    othello = []
    for m in range(M):                                  # 돌을 놓을 자리와 돌의 색상을 리스트로 받음
        othello.append(list(map(int, input().split())))
    board = [[0] * N for _ in range(N)]                 # 크기가 N은 오셀로 행렬을 board에 저장

    # 시작점 돌 놓기기
    board[N // 2 - 1][N // 2 - 1] = 2                   # 백돌을 중앙의 좌상에 놓음
    board[N // 2 - 1][N // 2] = 1                       # 흑돌을 중앙의 우상에 놓음
    board[N // 2][N // 2 - 1] = 1                       # 흑돌을 중앙의 좌하에 놓음
    board[N // 2][N // 2] = 2                           # 백돌을 중앙의 우하에 놓음

    # 델타 탐색
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]                    # 상 우 하 좌 # 좌상 우상 우하 좌하
    dy = [0, 1, 0, -1, -1, 1, 1, -1]                    # 상 우 하 좌 # 좌상 우상 우하 좌하

    # 돌 놓기
    for a in othello:                                   # othello 리스트를 반복해서
        y, x, c = a                                     # 0번 인덱스 값 = 열 / 1번 인덱스 값 = 행 / 2번 인덱스 값 = 돌의 색
        y = y - 1                                       # 0부터 시작하는 판에 맞게 -1을 해줌
        x = x - 1                                       # 0부터 시작하는 판에 맞게 -1을 해줌
        board[x][y] = c                                 # 좌표에 돌을 놓고

        # 돌 확인(가로 세로 대각선)
        for d in range(8):                              # 델타 탐색을 '상 우 하 좌  좌상 우상 우하 좌하' 순서로 한다
            for n in range(1, N):                       # 한 칸씩 이동하며 돌을 확인할 때
                if 0 <= x+dx[d]*n <= N-1 and 0 <= y+dy[d]*n <= N-1:     # 돌이 오셀로 판 안에 있는 경우만 확인
                    if board[x+dx[d]*n][y+dy[d]*n] == c:                # 만약 확인한 돌이 내돌과 같다면
                        for m in range(1, n):           # 여태 왔던 길을 반복하여
                            board[x + dx[d] * m][y + dy[d] * m] = c     # 같은 돌의 색으로 바꾼후 반복문을 종료한다
                        break
                    elif board[x+dx[d]*n][y+dy[d]*n] == 0:              # 만약 빈자리가 나오면 반복문을 종료하고
                        break
                    else:                               # 다른 색상 돌이 나오면 패스한다
                        pass

    else:                                               # 모든 돌을 놓고 난 후
        white = 0                                       # 흰돌의 개수를 저장할 변수를 만들고
        black = 0                                       # 검은돌의 개수를 저장할 변수를 만든다
        for i in range(N):                              # 오셀로 판의 행을 반복하고
            for j in range(N):                          # 오셀로 판의 열을 반복해서
                if board[i][j] == 1:                    # 검은 돌이 나오면
                    black += 1                          # black에 1을 더하고
                elif board[i][j] == 2:                  # 흰 돌이 나오면
                    white += 1                          # white에 1을 더한다
        print(f'#{t+1}', black, white)
