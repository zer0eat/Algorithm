# 침투_BOJ13565

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
M, N = map(int, input().split())                    # M 행의 길이 / N 열의 길이를 input 받고
fiber = [list(input().strip()) for _ in range(M)]   # 섬유 물질의 정보를 행렬로 input 받고
visited = [[0]*N for _ in range(M)]                 # 방문표시를 할 행렬을 생성한다
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]              # 4방향으로 이동할 리스트를 생성하고
for i in range(N):                                  # 열을 반복해서
    if fiber[0][i] == '0' and visited[0][i] == 0:   # 첫번째 열에 전류가 통하면서 방문 전이라면
        lst = deque([[0, i]])                       # 전류가 통하는 시작점을 넣은 deque를 생성하고
        visited[0][i] = 1                           # 방문표시를하고
        while lst:                                  # lst가 빌때까지 반복해서
            r, c = lst.popleft()                    # lst에서 popleft를 하고
            for t in range(4):                      # 4방향 이동을 반복해서
                x = r + d[t][0]                     # 이동한 행을 저장하고
                y = c + d[t][1]                     # 이동한 열을 저장해서
                if 0<=x<M and 0<=y<N:               # 이동한 위치가 섬유물질 내에 있으면서
                    if fiber[x][y] == '0' and visited[x][y] == 0:   # 이동한 위치가 전류가 통하면서 방문전이라면
                        visited[x][y] = 1           # 방문표시를 하고
                        lst.append([x, y])          # lst에 이동한 위치를 append한다
                    if x == M-1:                    # 만약 inner side에 도달했다면
                        print('YES')                # YES를 출력하고
                        quit()                      # 종료한다
else:                                               # for문을 모두 돌아도 inner side에 도달하지 못했다면
    print('NO')                                     # NO를 출력한다