# 뱀_BOJ3190

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())                                        # board의 크기를 input 받고
board = [[0]*N for _ in range(N)]                       # board를 행렬로 생성하고
K = int(input())                                        # 사과의 개수를 input 받아
for k in range(K):                                      # 사과의 수를 반복해서
    r, c = map(int, input().split())                    # r 사과 위치의 행 / c 사과 위치의 열을 input받고
    board[r-1][c-1] = 1                                 # board에 사과의 위치를 표시하고
L = int(input())                                        # 뱀의 방향전환 횟수를 input 받고
snake = deque([[0, 0]])                                 # 시작점에 있는 뱀 deque를 생헌다
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]                  # 4방향으로 델타이동할 리스트를 생성하고
cnt = 0                                                 # 이동횟수를 저장할 변수를 생성하고
dir = 0                                                 # 이동방향을 표시할 변수를 생성한다
for l in range(L+1):                                    # 뱀의 방향전환 횟수+1을 반복해서
    if l == L:                                          # 방향전환을 모두 했다면
        X = 10000                                       # 이동횟수를 최댓값으로 저장하고
    else:                                               # 방향전환 횟수가 남았다면
        X, C = input().split()                          # X 이동횟수 / C 방향전환 방향을 input 받는다
    while cnt < int(X):                                 # cnt가 X가 될때까지 반복해서
        cnt += 1                                        # cnt를 1 추가하고
        x = snake[-1][0] + d[dir][0]                    # 뱀의 이동방향의 행을 저장하고
        y = snake[-1][1] + d[dir][1]                    # 뱀의 이동방향의 열을 저장해서
        if 0<=x<N and 0<=y<N and ([x, y] not in snake): # 이동한 곳이 board 내에 있고 뱀의 몸과 부딪히지 않는다면
            if board[x][y] == 1:                        # 이동한 곳에 사과가 있다면
                board[x][y] = 0                         # 사과를 먹고 board의 사과를 없애주고
            else:                                       # 이동한 곳에 사과가 없다면
                tail = snake.popleft()                  # 길이를 유지하기 위해 꼬리를 빼주고
            snake.append([x, y])                        # 이동한 곳에 머리를 추가해준다
        else:                                           # 이동한 곳이 board 밖이거나 뱀의 몸과 부딪히면
            print(cnt)                                  # cnt를 출력하고
            quit()                                      # 종료한다
    else:                                               # cnt가 X가 되었다면
        if C == 'D':                                    # 방향전환이 D라면
            dir += 1                                    # dir를 1추가해서 오른쪽으로 전환하고
        else:                                           # 방향전환이 L이라면
            dir -= 1                                    # dir를 1빼서 왼쪽으로 전환하고
        dir = (dir+4) % 4                               # 0~3사이의 값이 되도록