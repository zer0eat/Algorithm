# 재미있는오셀로게임_4615

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from pprint import pprint

#  input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스 반복
    N, M = map(int, input().split())                # N = 오셀로보드의 크기 / M = 놓을 돌의 수
    board = [[0] * N for _ in range(N)]             # 크기가 N은 오셀로 행렬을 board에 저장
    for n in range(4):                              # 시작할 때 중앙에 흑돌과 백돌을 대각선으로 놓고 시작
        board[N//2][N//2] = 2                       # 백돌을 중앙의 우하에 놓음
        board[N//2 - 1][N//2 - 1] = 2               # 백돌을 중앙의 좌상에 놓음
        board[N//2 - 1][N//2] = 1                   # 흑돌을 중앙의 좌하에 놓음
        board[N//2][N//2 - 1] = 1                   # 흑돌을 중앙의 우상에 놓음

    dx = [-1, 0, 1, 0]                              # 상/우/하/좌
    dy = [0, 1, 0, -1]

    dxx = [-1, 1, 1, -1]                            # 우상/우하/좌하/좌상
    dyy = [1, 1, -1, -1]
    for m in range(M):                              # 돌을 놓을 횟수만큼 반복할 때
        col, row, color = map(int, input().split())     # 입력받은 첫번째 값을 col / 두번째 값을 row / 세번째 값을 color로 저장한다
        if board[row-1][col-1] == 0:                    # 놓을 자리가 빈자리 일 때
            flag = False                                # 돌을 놓을 수 있는 자리인지 확인하기 위해 flag를 False로 설치하고
            for w in range(4):                          # 상/우/하/좌를 살펴보기 위해 델타탐색을 반복할 때
                if 0 <= row - 1 + dx[w] < N and 0 <= col - 1 + dy[w] < N: # 탐색하는 지점이 행렬 범위 안일 때
                    if board[row-1][col-1] == 0 and board[row - 1 + dx[w]][col - 1 + dy[w]] != color and board[row - 1 + dx[w]][col - 1 + dy[w]] != 0:  # 비어있는 자리이고 옆 돌이 비어있지 않고 다른색 돌인 경우
                        flag = True                 # 돌을 놓을 수 있는 자리이므로 flag를 True로 바꾼 후
                        if w == 0:                  # 델타 탐색으로 윗방향을 탐색한다
                            for z in range(1, N):   # 한칸 씩 앞을 확인하기 위해 반복문을 사용하여
                                if 0 <= row - 1 + dx[w] * z < N and 0 <= col - 1 + dy[w] * z < N:       # 행렬 범위 내에 있는 경우
                                    if board[row - 1 + dx[w] * z][col - 1 + dy[w] * z] == 0:            # 돌이 없이 빈자리가 나오면 반복문을 break
                                        break
                                    elif board[row - 1 + dx[w] * z][col - 1 + dy[w] * z] == color:      # 다른색 돌이 나오다 같은색 돌이 나온지점에서
                                        n = 0                                                           # 이동을 위한 변수 n을 생성하고
                                        while 1:                                                        # 반복문을 돌려
                                            n -= 1                                                      # 한칸씩 뒤로 이동하며
                                            if 0 <= row - 1 + n < N:                                    # 행 범위 안에서
                                                if board[row - 1 + n][col - 1] != color and board[row - 1 + n][col - 1] != 0:   # 다른색 돌들을
                                                    board[row - 1 + n][col - 1] = color                 # color의 돌로 뒤집어준다
                                                else:
                                                    break
                                            else:
                                                break
                                        break
                        elif w == 2:                # 위와 같은 방법으로 아래쪽을 탐색한다.
                            for z in range(1, N):
                                if 0 <= row - 1 + dx[w] * z < N and 0 <= col - 1 + dy[w] * z < N:
                                    if board[row - 1 + dx[w] * z][col - 1 + dy[w] * z] == 0:
                                        break
                                    elif board[row - 1 + dx[w] * z][col - 1 + dy[w] * z] == color:
                                        n = 0
                                        while 1:
                                            n += 1
                                            if 0 <= row - 1 + n < N:
                                                if board[row - 1 + n][col - 1] != color and board[row - 1 + n][col - 1] != 0:
                                                    board[row - 1 + n][col - 1] = color
                                                else:
                                                    break
                                            else:
                                                break
                                        break
                        elif w == 1:                # 위와 같은 방법으로 오른쪽을 탐색한다.
                            for z in range(1, N):
                                if 0 <= row - 1 + dx[w] * z < N and 0 <= col - 1 + dy[w] * z < N:
                                    if board[row - 1 + dx[w] * z][col - 1 + dy[w] * z] == 0:
                                        break
                                    elif board[row - 1 + dx[w] * z][col - 1 + dy[w] * z] == color:
                                        n = 0
                                        while 1:
                                            n += 1
                                            if 0 <= col - 1 + n < N:
                                                if board[row - 1][col - 1 + n] != color and board[row - 1][col - 1 + n] != 0:
                                                    board[row - 1][col - 1 + n] = color
                                                else:
                                                    break
                                            else:
                                                break
                                        break
                        elif w == 3:                # 위와 같은 방법으로 왼쪽을 탐색한다.
                            for z in range(1, N):
                                if 0 <= row - 1 + dx[w] * z < N and 0 <= col - 1 + dy[w] * z < N:
                                    if board[row - 1 + dx[w] * z][col - 1 + dy[w] * z] == 0:
                                        break
                                    elif board[row - 1 + dx[w] * z][col - 1 + dy[w] * z] == color:
                                        n = 0
                                        while 1:
                                            n -= 1
                                            if 0 <= col - 1 + n < N:
                                                if board[row - 1][col - 1 + n] != color and board[row - 1][col - 1 + n] != 0:
                                                    board[row - 1][col - 1 + n] = color
                                                else:
                                                    break
                                            else:
                                                break
                                        break

                if 0 <= row - 1 + dxx[w] < N and 0 <= col - 1 + dyy[w] < N:         # 위와 같은 방법으로 대각선 좌상/좌하/우하/우상도 탐색한다.
                    if board[row-1][col-1] == 0 and board[row - 1 + dxx[w]][col - 1 + dyy[w]] != color and board[row - 1 + dxx[w]][col - 1 + dyy[w]] != 0:
                        flag = True
                        if w == 0:
                            for z in range(1, N):
                                if 0 <= row - 1 + dxx[w]*z < N and 0 <= col - 1 + dyy[w]*z < N:
                                    if board[row - 1 + dxx[w] * z][col - 1 + dyy[w] * z] == 0:
                                        break
                                    elif board[row - 1 + dxx[w]*z][col - 1 + dyy[w]*z] == color:
                                        n = 0
                                        while 1:
                                            n += 1
                                            if 0 <= row - 1 - n < N and 0 <= col - 1 + n < N:
                                                if board[row - 1 - n][col - 1 + n] != color and board[row - 1 - n][col - 1 + n] != 0:
                                                    board[row - 1 - n][col - 1 + n] = color
                                                else:
                                                    break
                                            else:
                                                break
                                        break
                        elif w == 1:
                            for z in range(1, N):
                                if 0 <= row - 1 + dxx[w]*z < N and 0 <= col - 1 + dyy[w]*z < N:
                                    if board[row - 1 + dxx[w] * z][col - 1 + dyy[w] * z] == 0:
                                        break
                                    elif board[row - 1 + dxx[w]*z][col - 1 + dyy[w]*z] == color:
                                        n = 0
                                        while 1:
                                            n += 1
                                            if 0 <= row - 1 + n < N and 0 <= col - 1 + n < N:
                                                if board[row - 1 + n][col - 1 + n] != color and board[row - 1 + n][col - 1 + n] != 0:
                                                    board[row - 1 + n][col - 1 + n] = color
                                                else:
                                                    break
                                            else:
                                                break
                                        break
                        elif w == 2:
                            for z in range(1, N):
                                if 0 <= row - 1 + dxx[w] * z < N and 0 <= col - 1 + dyy[w] * z < N:
                                    if board[row - 1 + dxx[w] * z][col - 1 + dyy[w] * z] == 0:
                                        break
                                    elif board[row - 1 + dxx[w] * z][col - 1 + dyy[w] * z] == color:
                                        n = 0
                                        while 1:
                                            n += 1
                                            if 0 <= row - 1 + n < N and 0 <= col - 1 - n < N:
                                                if board[row - 1 + n][col - 1 - n] != color and board[row - 1 + n][col - 1 - n] != 0:
                                                    board[row - 1 + n][col - 1 - n] = color
                                                else:
                                                    break
                                            else:
                                                break
                                        break
                        elif w == 3:
                            for z in range(1, N):
                                if 0 <= row - 1 + dxx[w] * z < N and 0 <= col - 1 + dyy[w] * z < N:
                                    if board[row - 1 + dxx[w] * z][col - 1 + dyy[w] * z] == 0:
                                        break
                                    elif board[row - 1 + dxx[w] * z][col - 1 + dyy[w] * z] == color:
                                        n = 0
                                        while 1:
                                            n += 1
                                            if 0 <= row - 1 - n < N and 0 <= col - 1 - n < N:
                                                if board[row - 1 - n][col - 1 - n] != color and board[row - 1 - n][col - 1 - n] != 0:
                                                    board[row - 1 - n][col - 1 - n] = color
                                                else:
                                                    break
                                            else:
                                                break
                                        break
            else:
                if flag == True:                        # 돌을 놓을 수 있는 경우로 flag가 바뀌었다면
                    board[row - 1][col - 1] = color     # 돌을 놓는다
    else:
        black = 0                                       # 검은색을 세기위한 변수
        white = 0                                       # 흰색을 세기위한 변수
        for i in range(N):                              # 행을 반복하고
            for j in range(N):                          # 열을 반복할 때
                if board[i][j] == 1:                    # 검은 돌이라면
                    black += 1                          # black에 1을 더해주고
                elif board[i][j] == 2:                  # 흰 돌이라면
                    white += 1                          # white에 1을 더해준다

        print(f'#{t+1}', black, white)