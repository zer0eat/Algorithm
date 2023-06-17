# 헌내기는 친구가 필요해_BOJ21736

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

def BFS(x, y):
    global ans, N, M                                            # 정답을 저장할 변수, 행, 열의 크기를 global로 설정
    tmp = deque([[x, y]])                                       # tmp에 도연이의 위치를 넣은 deque 생성
    while tmp:                                                  # tmp가 빌 때까지 반복해서
        x, y = tmp.popleft()                                    # 선입 된 위치 정보를 x,y로 pop한다
        if visited[x][y] == 0:                                  # 해당 위치가 방문 전이라면
            visited[x][y] = 1                                   # 방문표시를 한 후
            if jido[x][y] == 'P':                               # 사람을 만날 수 있다면
                ans += 1                                        # ans에 1을 추가하고
            elif jido[x][y] == 'X':                             # 막다른 길이라면
                continue                                        # continue로 다음 과정을 건너뛴다
            for t in range(4):                                  # 델타탐색을 해서
                if 0 <= x + dx[t] < N and 0 <= y + dy[t] < M:   # 캠퍼스 내의 위치에서
                    if visited[x + dx[t]][y + dy[t]] == 0:      # 방문 전인 위치라면
                        tmp.append([x + dx[t], y + dy[t]])      # tmp에 해당 위치를 append한다

# input 받기
N, M = map(int, input().split())                                # N 캠퍼스의 행 / M 캠퍼스의 열
jido = [list(input().strip()) for _ in range(N)]                # 캠퍼스의 정보를 list로 input받고
dx = [-1, 0, 1, 0]                                              # 행의 델타탐색을 위한 리스트 생성(상우하좌)
dy = [0, 1, 0, -1]                                              # 열의 델타탐색을 위한 리스트 생성(상우하좌)
visited = [[0]*M for _ in range(N)]                             # 방문 표시를 할 리스트를 생성하고
ans = 0                                                         # 정답을 저장할 변수 생성
for i in range(N):                                              # 행을 반복하고
    for j in range(M):                                          # 열을 반복해서
        if jido[i][j] == 'I':                                   # 도연이가 있는 I 위치가 나왔다면
            BFS(i, j)                                           # BFS로 만날 수 있는 친구를 탐색
            if ans == 0:                                        # 만날 수 있는 친구가 0명이라면
                print('TT')                                     # TT를 출력하고
            else:                                               # 1명 이상이라면
                print(ans)                                      # 숫자를 출력한 후
            quit()                                              # 종료한다