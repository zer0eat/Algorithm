# 아기 상어_BOJ16236

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())                                            # 상어가 돌아다닐 수 있는 크기를 input 받고
sea = [list(map(int, input().split())) for _ in range(N)]   # 상어와 물고기의 위치를 input 받는다
size = 2                                                    # 상어의 크기를 저장할 변수를 생성하고
eat = 0                                                     # 상어가 먹은 먹이를 저장할 변수를 생성하고
ans = 0                                                     # 상어가 먹이를 잡아먹을 수 있는 시간을 저장할 변수를 생성한다
tmp = []                                                    # 상어의 위치를 저장할 리스트를 생성하고
for i in range(N):                                          # 행을 반복하고
    if tmp:                                                 # 상어의 위치를 찾았다면
        break                                               # for문을 break 한다
    for j in range(N):                                      # 열을 반복해서
        if sea[i][j] == 9:                                  # 상어의 위치를 찾았다면
            tmp = [[i, j]]                                  # tmp에 상어의 위치를 넣어 저장하고
            sea[i][j] = 0                                   # 상어의 위치를 0으로 바꾼 후
            break                                           # for문을 break한다
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]                      # 4방향으로 이동하기 위한 리스트를 생성하고
visited = [[0]*N for _ in range(N)]                         # 방문표시를 할 리스트를 생성한 후
cnt = 1                                                     # 상어가 이동한 시간을 저장할 변수를 생성한다
while tmp:                                                  # tmp가 빌때까지 반복해서
    tmp2 = []                                               # 상어가 이동한 위치를 저장할 리스트를 생성하고
    tmp3 = []                                               # 상어가 잡아먹은 물고기의 위치를 저장할 리스트를 생성한다
    for shark in tmp:                                       # 상어의 위치를 반복해서
        for t in range(4):                                  # 상어가 4방향으로 이동했을 때
            x = shark[0] + d[t][0]                          # 이동한 행을 x에 저장하고
            y = shark[1] + d[t][1]                          # 이동한 열을 y에 저장한 후
            if 0<=x<N and 0<=y<N and visited[x][y]==0:      # 이동한 위치가 행렬 내에 있고 방문 전이라면
                if sea[x][y] != 0 and sea[x][y] < size:     # 이동한 위치에 먹을 수 있는 물고기가 있다면
                    tmp3.append([x, y])                     # 해당 위치를 tmp3에 저장한 후
                    visited[x][y] = 1                       # 방문표시한다
                elif sea[x][y] == size:                     # 이동한 위치에 같은 크기의 물고기가 있다면 먹을 순 없고 이동할 수 있으므로
                    tmp2.append([x,y])                      # 해당 위치를 tmp2에 저장한 후
                    visited[x][y] = 1                       # 방문표시한다
                elif sea[x][y] == 0:                        # 이동한 위치가 비어있다면
                    tmp2.append([x, y])                     # 해당 위치를 tmp2에 저장한 후
                    visited[x][y] = 1                       # 방문표시한다
    else:                                                   # 상어의 모든 위치를 반복했다면
        if tmp3:                                            # 이동후 잡아먹을 물고기가 있는 경우에
            tmp3.sort()                                     # 물고기의 위치를 정렬해서
            ans += cnt                                      # 상어가 이동한 시간을 ans에 더해주고
            cnt = 1                                         # 이동한 시간을 초기화 해준 후
            eat += 1                                        # 상어가 먹은 먹이를 1 더해준다
            if eat == size:                                 # 상어가 자신의 사이즈만큼 먹이를 먹었다면
                eat = 0                                     # 먹이를 초기화하고
                size += 1                                   # 상어의 크기를 1 증가시킨다
            tmp = [tmp3[0]]                                 # tmp에 상어가 잡아먹은 물고기의 위치를 저장하고
            sea[tmp3[0][0]][tmp3[0][1]] = 0                 # 잡아먹은 위치는 0으로 빈공간 표시를 한 후
            visited = [[0] * N for _ in range(N)]           # 방문 표시를 할 리스트를 초기화하고 while문을 반복한다
        else:                                               # 이동 후 잡아먹을 물고기가 없는 경우
            tmp = tmp2[:]                                   # tmp에 상어가 이동한 위치인 tmp2를 저장하고
            cnt += 1                                        # 이동한 시간을 1 추가한 후 while문을 반복한다
print(ans)                                                  # while문이 종료되어 더이상 잡아 먹을 수 있는 물고기가 없다면 최소 이동 시간을 출력한다