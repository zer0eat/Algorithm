# 양_BOJ3184.py

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
R, C = map(int, input().split())                                            # R 마당의 행 / C 마당의 열을 input 받고
field = [list(input().strip()) for _ in range(R)]                           # 마당의 정보를 행렬로 input 받는다
visited = [[0]*C for _ in range(R)]                                         # 방문표시를 할 행렬을 생성하고
d = [[1,0],[-1,0],[0,1],[0,-1]]                                             # 4방향으로 이동할 리스트를 생성한다
sheep, wolf = 0, 0                                                          # 하루 후 양과 늑대의 수를 셀 변수를 생성하고
for i in range(R):                                                          # 행을 반복하고
    for j in range(C):                                                      # 열을 반복해서
        if field[i][j] != '#' and visited[i][j] == 0:                       # 해당원소가 울타리가 아니고 방문전이라면
            tmp_sheep, tmp_wolf = 0,0                                       # 해당 구역 안의 양과 늑대를 셀 변수를 생성하고
            lst = deque([[i, j]])                                           # 시작점을 리스트에 넣어 deque를 생성한다
            visited[i][j] = 1                                               # 시작점을 방문표시하고
            while lst:                                                      # lst가 빌때까지 반복해서
                r, c = lst.popleft()                                        # deuqe에서 원소의 행과 열을 꺼내서
                if field[r][c] == 'o':                                      # 해당 원소가 양이라면
                    tmp_sheep += 1                                          # 구역 내 양의 수를 1 증가시키고
                elif field[r][c] == 'v':                                    # 해당원소가 늑대라면
                    tmp_wolf += 1                                           # 구역 내 늑대의 수를 1 증가시킨다
                for t in range(4):                                          # 4방향 탐색을 해서
                    x = r + d[t][0]                                         # 이동 후 행의 위치를 x에 저장하고
                    y = c + d[t][1]                                         # 이동 후 열의 위치를 y에 저장해서
                    if 0<=x<R and 0<=y<C:                                   # 이동 후 위치가 마당 내에 있고
                        if field[x][y] != '#' and visited[x][y] == 0:       # 이동 위치가 울타리가 아니면서 방문 전이라면
                            lst.append([x,y])                               # lst에 이동 위치를 append하고
                            visited[x][y] = 1                               # 방문표시한다
            else:                                                           # lst가 빌때까지 모두 반복했다면
                if tmp_sheep > tmp_wolf:                                    # 구역내 양의 수가 늑대의 수보다 많다면
                    sheep += tmp_sheep                                      # 하루 후 양의 수에 구역 내 양의 수를 더하고
                else:                                                       # 늑대의 수가 양의 수보다 같거나 크다면
                    wolf += tmp_wolf                                        # 하루 후 늑대의 수에 구역 내 늑대의 수를 더한다
print(sheep, wolf)                                                          # 모든 탐색을 마친 후 하루 후 남아있는 양과 늑대의 수를 출력한다