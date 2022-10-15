# 토마토_BOJ7576

# input.txt 열기
import sys
sys.stdin = open('input.txt')
from collections import deque

# input 받기
M, N = map(int, sys.stdin.readline().split())                                           # M 열의 길이 / N 행의 길이
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]               # 토마토의 상태를 input받아 저장한 리스트
visited = [[0]*M for _ in range(N)]                                                     # 토마토 방문여부를 확인할 빈 리스트
q = deque()                                                                             # q를 deque로 생성

dx = [-1, 0, 1, 0]                                                                      # 델타탐색을 할 때 행의방향으로 이동하기 위한 리스트
dy = [0, 1, 0, -1]                                                                      # 델타탐색을 할 때 열의방향으로 이동하기 위한 리스트

minus = 0                                                                               # 마이너스의 개수를 저장할 변수
for i in range(N):                                                                      # 행을 반복하고
    for j in range(M):                                                                  # 열을 반복해서
        if tomato[i][j] == 1 and visited[i][j] == 0:                                    # 이미 익은 토마토라면
            visited[i][j] = 1                                                           # visited리스트에 방문표시를 하고
            q.append([i,j,0])                                                           # q에 [행,열,방문깊이]를 append 한다
        elif tomato[i][j] == -1:                                                        # 반약 빈칸이라면
            minus += 1                                                                  # minus에 1을 추가한다

while q:                                                                                # q가 빌떄까지 반복해서
    A = q.popleft()                                                                     # q의 맨 앞에서 하나 pop해
    i = A[0]                                                                            # i에 A[0]을 저장하고
    j = A[1]                                                                            # j에 A[1]를 저장한다
    for k in range(4):                                                                  # 델타탐색을 하여
        if 0 <= i+dx[k] < N and 0 <= j+dy[k] < M:                                       # 행렬의 범위 내에서
            if tomato[i+dx[k]][j+dy[k]] == 0 and visited[i+dx[k]][j+dy[k]] == 0:        # 익지않았으면서 방문 전인 곳에 방문했다면
                visited[i + dx[k]][j + dy[k]] = 1                                       # 방문표시를 하고
                q.append([i + dx[k], j + dy[k], A[2]+1])                                # q에 [행,열,방문깊이]를 append 한다

ans = M * N                                                                             # 토마토의 모든 칸수를 저장한 변수를 생성하고
for v in visited:                                                                       # 방문표시를 반복하며
    ans -= sum(v)                                                                       # 방문한 곳을 모두 ans에서 빼준다
else:                                                                                   # 모두 탐색을 마쳤다면
    ans -= minus                                                                        # 방문하지 않은곳 중 빈칸을 ans에서 빼준다

if ans == 0:                                                                            # ans의 값이 0이되면 모두 익었으므로
    print(A[2])                                                                         # 마지막 깊이를 출력하고
else:                                                                                   # ans의 값이 0이 아니라면
    print(-1)                                                                           # 익지않은 토마토가 있으므로 -1을 출력한다