# 점프왕 쩰리 (Small)_BOJ16173

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())                            # 게임 구역의 크기를 input 받고
jelly = [list(map(int, input().split())) for _ in range(N)] # 게임판의 맵을 행렬 input 받는다
visited = [[0]*N for _ in range(N)]         # 방문기록을 저장할 행렬을 생성한다
d = [[0, 1], [1, 0]]                        # 2방향으로 이동할 리스트를 생성하고
lst = deque([[0, 0]])                       # 시작점을 넣은 deque를 생성하고
visited[0][0] = 1                           # 시작점을 방문표시를 한다
while lst:                                  # lst가 빌때까지 반복해서
    r, c = lst.popleft()                    # lst에서 leftpop으로 이동위치를 꺼내고
    if [r, c] == [N-1, N-1]:                # 도착지에 도착했다면
        print('HaruHaru')                   # HaruHaru를 출력하고
        break                               # while문을 break한다
    for t in range(2):                      # 두방향 이동을 반복해서
        x = r + d[t][0]*jelly[r][c]         # 이동한 곳의 행을 x에 저장하고
        y = c + d[t][1]*jelly[r][c]         # 이동한 곳의 열을 y에 저장한다
        if 0<=x<N and 0<=y<N:               # 이동한 곳이 게임판 맵 안에 있고
            if visited[x][y] == 0:          # 방문 전이라면
                lst.append([x, y])          # lst에 이동한 곳을 append하고
                visited[x][y] = 1           # 방문표시한다
else:                                       # 도착지에 도착하지 못했다면
    print('Hing')                           # Hing을 출력한다