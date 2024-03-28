# 보물섬_BOJ2589

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
R, C = map(int, input().split())                                            # 지도의 행과 열을 input 받고
jido = [list(input().strip()) for _ in range(R)]                            # 지도의 땅과 바다 정보를 리스트로 input 받는다
ans = 0                                                                     # 정답을 저장할 변수를 생성하고
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]                                      # 4방향 이동을 위한 리스트를 생성한다
for r in range(R):                                                          # 행을 반복하고
    for c in range(C):                                                      # 열을 반복해서
        if jido[r][c] == 'L':                                               # r,c가 땅이라면
            visited = [[0]*C for _ in range(R)]                             # 방문표시를 할 리스트를 생성하고
            que = deque([[r, c]])                                           # 시작점을 넣은 deque를 생성하고
            visited[r][c] = 1                                               # r,c를 방문표시한다
            while que:                                                      # que가 빌때까지 반복해서
                x, y = que.popleft()                                        # que에서 위치를 popleft하고
                for i in range(4):                                          # 4방향을 반복해서
                    xx = x + d[i][0]                                        # 이동후 행을 xx에 저장하고
                    yy = y + d[i][1]                                        # 이동후 열을 yy에 저장한다
                    if 0<=xx<R and 0<=yy<C:                                 # 이동 후 위치가 jido 안에 있고
                        if jido[xx][yy] == 'L' and visited[xx][yy] == 0:    # 이동 후 위치가 땅이고 방문 전이라면
                            visited[xx][yy] = visited[x][y] + 1             # 이동 후 위치에 몇칸 만에 갈 수 있는지 저장하고
                            ans = max(visited[xx][yy], ans)                 # 현재 저장된 가장 먼 거리와 현재까지 이동한 거리 중 더 큰 값을 저장한다
                            que.append([xx, yy])                            # que에 이동한 위치를 append한다
print(ans-1)                                                                # 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력한다