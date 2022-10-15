# 토마토_BOJ7576

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from collections import deque

# input 받기
M, N = map(int, sys.stdin.readline().split())                                   # M 열의 길이 / N 행의 길이
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]       # 토마토의 상태를 input받아 저장한 리스트
q = deque()                                                                     # q를 deque로 생성

dx = [-1, 0, 1, 0]                                                              # 델타탐색을 할 때 행의방향으로 이동하기 위한 리스트
dy = [0, 1, 0, -1]                                                              # 델타탐색을 할 때 열의방향으로 이동하기 위한 리스트

for i in range(N):                                                              # 행을 반복하고
    for j in range(M):                                                          # 열을 반복해서
        if tomato[i][j] == 1:                                                   # 이미 익은 토마토라면
            q.append([i,j,0])                                                   # q에 [행,열,방문깊이]를 append 한다

while q:                                                                        # q가 빌떄까지 반복해서
    A = q.popleft()                                                             # q의 맨 앞에서 하나 pop해
    i = A[0]                                                                    # i에 A[0]을 저장하고
    j = A[1]                                                                    # j에 A[1]를 저장한다
    for k in range(4):                                                          # 델타탐색을 하여
        if 0 <= i+dx[k] < N and 0 <= j+dy[k] < M:                               # 행렬의 범위 내에서
            if tomato[i+dx[k]][j+dy[k]] == 0 :                                  # 토마토가 익지 않은 곳이라면
                tomato[i + dx[k]][j + dy[k]] = 1                                # 익은 표시로 바꿔준 후
                q.append([i + dx[k], j + dy[k], A[2]+1])                        # 해당위치를 q에 [행,열,방문깊이]를 append 한다

for i in range(N):                                                              # 행을 반복하고
    for j in range(M):                                                          # 열을 반복해서
        if tomato[i][j] == 0:                                                   # 익지 않은 토마토가 있다면
            print(-1)                                                           # -1을 출력하고
            exit()                                                              # 종료하고
else:                                                                           # 모두 익은 토마토거나 빈칸이라면
    print(A[2])                                                                 # 마지막 깊이를 출력한다