# 토마토_BOJ7569

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from collections import deque

# input 받기
M, N, H = map(int, sys.stdin.readline().split())                                        # M 열의 길이 / N 행의 길이 / H 상자의 수
tomato = []                                                                             # 토마토를 저장할 빈리스트를 만들고
for h in range(H):                                                                      # 토마토의 층수만큼 반복해서
    tomato.append([list(map(int, sys.stdin.readline().split())) for _ in range(N)])     # 토마토의 한층의 정보를 input 받아 tomato에 append
q = deque()                                                                             # q를 deque로 생성

dx = [-1, 0, 1, 0]                                                                      # 델타탐색을 할 때 행의방향으로 이동하기 위한 리스트
dy = [0, 1, 0, -1]                                                                      # 델타탐색을 할 때 열의방향으로 이동하기 위한 리스트
dh = [-1,1]                                                                             # 델타탐색을 할 때 위층 아래층 방향으로 이동하기 위한 리스트
for h in range(H):                                                                      # 층을 반복하고
    for i in range(N):                                                                  # 행을 반복하고
        for j in range(M):                                                              # 열을 반복해서
            if tomato[h][i][j] == 1:                                                    # 이미 익은 토마토라면
                q.append([h,i,j,0])                                                     # q에 [층,행,열,방문깊이]를 append 한다

while q:                                                                                # q가 빌떄까지 반복해서
    A = q.popleft()                                                                     # q의 맨 앞에서 하나 pop해
    h = A[0]                                                                            # h에 A[0]을 저장하고
    i = A[1]                                                                            # i에 A[1]을 저장하고
    j = A[2]                                                                            # j에 A[2]를 저장한다
    for g in range(2):                                                                  # 위층 아래층 델타탐색을 해서
        if 0 <= h + dh[g]< H:                                                           # 층수 범위 내에서
            if tomato[h + dh[g]][i][j] == 0:                                            # 토마토가 익지 않은 곳이라면
                tomato[h + dh[g]][i][j] = 1                                             # 익은 표시로 바꿔준 후
                q.append([h + dh[g], i, j, A[3]+1])                                     # 해당위치를 q에 [층,행,열,방문깊이]를 append 한다
    for k in range(4):                                                                  # 델타탐색을 하여
        if 0 <= i+dx[k] < N and 0 <= j+dy[k] < M:                                       # 행렬의 범위 내에서
            if tomato[h][i+dx[k]][j+dy[k]] == 0:                                        # 토마토가 익지 않은 곳이라면
                tomato[h][i + dx[k]][j + dy[k]] = 1                                     # 익은 표시로 바꿔준 후
                q.append([h, i + dx[k], j + dy[k], A[3]+1])                             # 해당위치를 q에 [층,행,열,방문깊이]를 append 한다

for h in range(H):                                                                      # 층을 반복하고
    for i in range(N):                                                                  # 행을 반복하고
        for j in range(M):                                                              # 열을 반복해서
            if tomato[h][i][j] == 0:                                                    # 익지 않은 토마토가 있다면
                print(-1)                                                               # -1을 출력하고
                exit()                                                                  # 종료하고
else:                                                                                   # 모두 익은 토마토거나 빈칸이라면
    print(A[3])                                                                         # 마지막 깊이를 출력한다