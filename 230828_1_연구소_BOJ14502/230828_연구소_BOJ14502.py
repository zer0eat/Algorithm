# 연구소_BOJ14502

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import copy
from collections import deque

# input 받기
N, M = map(int, sys.stdin.readline().split())                   # N 연구소의 행 / M 연구소의 열을 input받고
lap = [list(map(int, input().split())) for _ in range(N)]       # 연구소 지도를 행렬로 input 받는다
d = [[-1,0],[1,0],[0,-1],[0,1]]                                 # 상하좌우 이동을 할 수 있도록 리스트를 생성하고
ans = 0                                                         # 안전 영역의 수를 저장할 변수를 만든다

def make_wall(count):                                           # 벽을 세울 함수를 만들고
    if count == 3:                                              # 벽이 3개 세워졌다면
        bfs()                                                   # bfs 항수로 안전구역을 찾고
        return                                                  # return한다
    for i in range(N):                                          # 행을 반복하고
        for j in range(M):                                      # 열을 반복해서
            if lap[i][j] == 0:                                  # 빈 공간이 나왔으면
                lap[i][j] = 1                                   # 벽을 설치하고
                make_wall(count+1)                              # 설치개수를 1 추가하여 벽을 세우는 함수를 실행한다
                lap[i][j] = 0                                   # 벽을 제거한다

virus = deque()                                                 # 바이러스의 위치를 담을 deque를 생성하고
for i in range(N):                                              # 행을 반복하고
    for j in range(M):                                          # 열을 반복해서
        if lap[i][j] == 2:                                      # 바이러스가 나온다면
            virus.append([i, j])                                # 바이러스의 위치를 append 한다

def bfs():                                                      # 안전 영역의 수를 셀 함수를 만들고
    global ans                                                  # ans를 global 변수로 불러온다
    virus2 = copy.deepcopy(virus)                               # 바이러스의 위치를 복사하여 저장하고
    test_map = copy.deepcopy(lap)                               # 벽이 세워진 지도를 복사하여 저장한다
    while virus2:                                               # 바이러스가 빌때까지 반복해서
        x, y = virus2.popleft()                                 # 바이러스를 deque에서 꺼낸 후
        for i in range(4):                                      # 해당위치에서 상하좌우 4방향을 반복한다
            dx = x+d[i][0]                                      # 이동 행을 저장하고
            dy = y+d[i][1]                                      # 이동 열을 저장해서
            if (0<=dx<N) and (0<=dy<M):                         # 이동한 위치가 연구실 안이면서
                if test_map[dx][dy] == 0:                       # 이동한 위치가 벽이 아닌 공간이라면
                    test_map[dx][dy] = 2                        # 바이러스가 퍼졌음을 표시하고
                    virus2.append([dx,dy])                      # 퍼진 위치를 virus2 deque에 append 한다
    cnt = 0                                                     # 안전 영역을 셀 변수를 생성하고
    for i in range(N):                                          # 행을 반복하고
        for j in range(M):                                      # 열을 반복해서
            if test_map[i][j] == 0:                             # 해당 영역이 바이러스가 퍼지지 않았다면
                cnt += 1                                        # 안전 영역의 수를 추가한다
    ans = max(ans, cnt)                                         # ans와 cnt 중 더 안전 영역이 많은 수를 ans에 저장한다

make_wall(0)                                                    # 벽을 세우는 함수를 실행하고
print(ans)                                                      # 안전영역의 수를 출력한다