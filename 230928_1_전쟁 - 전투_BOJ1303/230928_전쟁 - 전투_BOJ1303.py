# 전쟁 - 전투_BOJ1303

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N, M = map(int, input().split())                            # N 전쟁터의 가로크기 / M 전쟁터의 세로크기를 input 받고
battleground = [list(input().strip()) for _ in range(M)]    # 전쟁터의 병사정보를 행렬로 input 받는다
visited = [[0]*N for _ in range(M)]                         # 방문표시를할 행렬을 생성하고
white, blue = 0, 0                                          # 흰 병사의 세력과 파란 병사의 세력을 저장할 변수를 생성하고
d= [[1,0],[-1,0],[0,1],[0,-1]]                              # 4방향으로 이동할 리스트를 생성한다
for i in range(M):                                          # 행을 반복하고
    for j in range(N):                                      # 열을 반복해서
        if visited[i][j] == 0:                              # 방문하지 않은 곳이라면
            if battleground[i][j] == 'W':                   # 해당 병사가 흰 옷이라면
                lst = deque([[i,j]])                        # 시작점을 넣은 deque를 생성하고
                visited[i][j] = 1                           # 시작점을 방문표시한다
                w = 0                                       # 시작점과 연결된 흰옷 병사의 수를 셀 변수를 생성하고
                while lst:                                  # lst가 빌때까지 반복해서
                    r, c = lst.popleft()                    # lst에서 행과 열을 popleft한다
                    w += 1                                  # 흰옷 병사의 수를 1 추가하고
                    for t in range(4):                      # 4방향 탐색을 진행해서
                        x = r + d[t][0]                     # 이동한 행을 x에 저장하고
                        y = c + d[t][1]                     # 이동한 열을 y에 저장해서
                        if 0<=x<M and 0<=y<N:               # 이동한 위치가 전쟁터 내라면
                            if visited[x][y] == 0 and battleground[x][y] == 'W':    # 이동한 위치가 방문 전이고 흰 병사일 때
                                visited[x][y] = 1           # 방문표시를 하고
                                lst.append([x, y])          # 이동위치를 lst에 append한다
                else:                                       # lst가 빌때까지 탐색했다면
                    white += w**2                           # 흰옷병사의 수의 제곱을 흰 병사의 세력에 더해준다
            else:                                           # 해당 병사가 파란 옷이라면
                lst = deque([[i, j]])                       # 시작점을 넣은 deque를 생성하고
                visited[i][j] = 1                           # 시작점을 방문표시한다
                b = 0                                       # 시작점과 연결된 파란옷 병사의 수를 셀 변수를 생성하고
                while lst:                                  # lst가 빌때까지 반복해서
                    r, c = lst.popleft()                    # lst에서 행과 열을 popleft한다
                    b += 1                                  # 파란옷 병사의 수를 1 추가하고
                    for t in range(4):                      # 4방향 탐색을 진행해서
                        x = r + d[t][0]                     # 이동한 행을 x에 저장하고
                        y = c + d[t][1]                     # 이동한 열을 y에 저장해서
                        if 0<=x<M and 0<=y<N:               # 이동한 위치가 전쟁터 내라면
                            if visited[x][y] == 0 and battleground[x][y] == 'B':    # 이동한 위치가 방문 전이고 파란 병사일 때
                                visited[x][y] = 1           # 방문표시를 하고
                                lst.append([x, y])          # 이동위치를 lst에 append한다
                else:                                       # lst가 빌때까지 탐색했다면
                    blue += b**2                            # 파란옷병사의 수의 제곱을 파란 병사의 세력에 더해준다
print(white, blue)                                          # 흰 병사와 파란 병사의 세력을 출력한다