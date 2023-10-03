# 벽 부수고 이동하기_BOJ2206

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N, M = map(int, input().split())                    # N 행의 길이 / M 열의 길이를 input 받고
jido = [list(input().strip()) for _ in range(N)]    # 벽 정보가 표시된 행렬을 input 받고
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]              # 4방향으로 이동할 리스트를 생성한다
visited = [[0]*M for _ in range(N)]                 # 방문표시를 할 행렬을 생성하고
lst = deque([[1, 0, 0]])                            # 이동횟수와 시작점을 넣은 deque를 생성한다
visited[0][0] = 1                                   # 시작점을 방문표시를 한다
while lst:                                          # lst가 빌때까지 반복해서
    cnt, r, c = lst.popleft()                       # 이동횟수와 이동위치를 popleft한다
    if r == N-1 and c == M-1:                       # 도착지에 도착했다면
        print(cnt)                                  # 최단거리를 출력하고
        break                                       # while문을 break한다
    for t in range(4):                              # 4방향을 반복해서
        x = r + d[t][0]                             # 이동한 행을 저장하고
        y = c + d[t][1]                             # 이동한 열을 저장한다
        if 0<=x<N and 0<=y<M:                       # 이동한 곳이 행렬 내에 있다면
            if visited[r][c] == 1 and jido[x][y] == '0' and visited[x][y] == 0:     # 벽을 부수기 전이고 이동한 곳이 벽이 아니면서 방문전이라면
                visited[x][y] = 1                   # 벽을 부수기 전으로 방문표시하고
                lst.append([cnt+1,x,y])             # 횟수와 이동위치를 append한다
            elif visited[r][c] == 2 and jido[x][y] == '0' and visited[x][y] == 0:   # 벽을 부순 후이고 이동한 곳이 벽이 아니면서 방문전이라면
                visited[x][y] = 2                   # 벽을 부순 후로 방문표시하고
                lst.append([cnt+1,x,y])             # 횟수와 이동위치를 append한다
            elif visited[r][c] == 1 and jido[x][y] == '1' and visited[x][y] == 0:   # 벽을 부수기 전이고 이동한 곳이 벽이면서 방문전이라면
                visited[x][y] = 2                   # 벽을 부순 후로 방문표시하고
                lst.append([cnt+1,x,y])             # 횟수와 이동위치를 append한다
            elif visited[r][c] == 1 and jido[x][y] == '0' and visited[x][y] == 2:   # 벽을 부수기 전이고 이동한 곳이 벽이 아니면서 벽을 부수고 방문한 후라면
                visited[x][y] = 1                   # 벽을 부수기 전으로 방문표시하고
                lst.append([cnt+1,x,y])             # 횟수와 이동위치를 append한다
else:                                               # 도착지에 도착하지 못했다면
    print(-1)                                       # -1을 출력한다