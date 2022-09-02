# 재미있는오셀로게임_4615

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from pprint import pprint

#  input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스 반복
    N, M = map(int, input().split())                # N = 오셀로보드의 크기 / M = 놓을 돌의 수

    othello = [list(map(int, input().split())) for _ in range(M)]

    board = [[0] * N for _ in range(N)]             # 크기가 N은 오셀로 행렬을 board에 저장

    board[N//2][N//2] = 2                           # 백돌을 중앙의 우하에 놓음
    board[N//2 - 1][N//2 - 1] = 2                   # 백돌을 중앙의 좌상에 놓음
    board[N//2 - 1][N//2] = 1                       # 흑돌을 중앙의 좌하에 놓음
    board[N//2][N//2 - 1] = 1                       # 흑돌을 중앙의 우상에 놓음

    dx = [-1, 0, 1, 0]                              # 상/우/하/좌
    dy = [0, 1, 0, -1]

    dxx = [-1, 1, 1, -1]                            # 우상/우하/좌하/좌상
    dyy = [1, 1, -1, -1]

    while othello:
        y, x, c = othello.pop(0)                    # y = 열, x = 행, c = 색

        if c == 1:                                  # 만약 검은색이라면
            for n in range(4):
                # 상/우/하/좌를 반복하여
                if 0 <= x - 1 + dx[n] < N and 0 <= y - 1 + dy[n] < N:   # 행렬 범위 내에서
                    if board[x - 1 + dx[n]][y - 1 + dy[n]] == 2:        # 옆돌이 흰돌이라면
                        for m in range(1, N):                           # 그 방향으로 계속 반복한다
                            if 0 <= x-1+dx[n]*m < N and 0 <= y-1+dy[n]*m < N:   # 행렬 범위 내에서
                                if board[x-1+dx[n]*m][y-1+dy[n]*m] == 0:        # 옆돌이 없다면
                                    break                                       # 반복문을 종료하고 돌을 놓지 않는다
                                if board[x-1+dx[n]*m][y-1+dy[n]*m] == 1:        # 옆돌이 검은돌이라면
                                    for k in range(1, m+1):                     # 여태 왔던 경로를 반복하여
                                        if board[x - 1 + dx[n] * k][y - 1 + dy[n] * k] == 2:    # 흰색돌을
                                            board[x - 1 + dx[n] * k][y - 1 + dy[n] * k] = 1     # 검은색돌로 바꾼다
                                    else:                               # 반복이 끝났다면 반복문을 종료한다
                                        break
                # 우상/우하/좌하/좌상를 반복하여
                if 0 <= x - 1 + dxx[n] < N and 0 <= y - 1 + dyy[n] < N: # 행렬 범위 내에서
                    if board[x - 1 + dxx[n]][y - 1 + dyy[n]] == 2:      # 옆돌이 흰돌이라면
                        for b in range(1, N):                           # 그 방향으로 계속 반복한다
                            if 0 <= x - 1 + dxx[n] * b < N and 0 <= y - 1 + dyy[n] * b < N: # 행렬 범위 내에서
                                if board[x - 1 + dxx[n] * b][y - 1 + dyy[n] * b] == 0:      # 옆돌이 없다면
                                    break                                                   # 반복문을 종료하고 돌을 놓지 않는다
                                if board[x - 1 + dxx[n] * b][y - 1 + dyy[n] * b] == 1:      # 옆돌이 검은돌이라면
                                    for j in range(1, b+1):                                 # 여태 왔던 경로를 반복하여
                                        if board[x - 1 + dxx[n] * j][y - 1 + dyy[n] * j] == 2:  # 흰색돌을
                                            board[x - 1 + dxx[n] * j][y - 1 + dyy[n] * j] = 1   # 검은색돌로 바꾼다
                                    else:                               # 반복이 끝났다면 반복문을 종료한다
                                        break
            else:                                                       # 모든 방향을 확인한 후 y,x에 돌을 놓는다
                board[x - 1][y - 1] = 1


        elif c == 2:                                # 만약 흰색이라면 위와 같은 조건으로 돌을 놓아준다
            for n in range(4):
                if 0 <= x - 1 + dx[n] < N and 0 <= y - 1 + dy[n] < N:
                    if board[x - 1 + dx[n]][y - 1 + dy[n]] == 1:
                        for m in range(1, N):
                            if 0 <= x-1+dx[n]*m < N and 0 <= y-1+dy[n]*m < N:
                                if board[x-1+dx[n]*m][y-1+dy[n]*m] == 0:
                                    break
                                if board[x-1+dx[n]*m][y-1+dy[n]*m] == 2:
                                    for k in range(1, m+1):
                                        if board[x - 1 + dx[n] * k][y - 1 + dy[n] * k] == 1:
                                            board[x - 1 + dx[n] * k][y - 1 + dy[n] * k] = 2
                                    else:
                                        break
                if 0 <= x - 1 + dxx[n] < N and 0 <= y - 1 + dyy[n] < N:
                    if board[x - 1 + dxx[n]][y - 1 + dyy[n]] == 1:
                        for b in range(1, N):
                            if 0 <= x - 1 + dxx[n] * b < N and 0 <= y - 1 + dyy[n] * b < N:
                                if board[x - 1 + dxx[n] * b][y - 1 + dyy[n] * b] == 0:
                                    break
                                if board[x - 1 + dxx[n] * b][y - 1 + dyy[n] * b] == 2:
                                    for j in range(1, b+1):
                                        if board[x - 1 + dxx[n] * j][y - 1 + dyy[n] * j] == 1:
                                            board[x - 1 + dxx[n] * j][y - 1 + dyy[n] * j] = 2
                                    else:
                                        break
            else:
                board[x - 1][y - 1] = 2
    else:                                       # 모든 돌을 놓았다면
        black = 0                               # 검은색 돌을 세줄 변수와
        white = 0                               # 흰색 돌을 세줄 변수를 만들고
        for i in range(N):                      # 오셀로 판의 행과
            for j in range(N):                  # 열을 반복해서
                if board[i][j] == 1:            # 검은 돌이나오면
                    black += 1                  # 블랙에 1을 더해주고
                elif board[i][j] == 2:          # 흰돌이 나오면
                    white += 1                  # 화이트에 1을 더해준다

    print(f'#{t + 1}', black, white)