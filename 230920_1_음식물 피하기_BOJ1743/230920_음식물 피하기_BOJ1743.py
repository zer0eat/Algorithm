# 음식물 피하기_BOJ1743

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10001)

# input 받기
N, M, K = map(int, input().split())     # N 행의 크기 / M 열의 크기 / K 쓰레기의 수를 input 받고
road = [[0]*M for _ in range(N)]        # 쓰레기를 표시할 행렬을 생성하고
visited = [[0]*M for _ in range(N)]     # 방문표시를 할 행렬을 생성한다
for i in range(K):                      # 쓰레기의 수를 반복해서
    x, y = map(int, input().split())    # 쓰레기의 위치를 input 받아서
    road[x-1][y-1] = 1                  # 해당위치에 표시를 한다

def dfs(i, j):
    global cnt                          # cnt를 global 변수로 선언한다
    visited[i][j] = 1                   # i,j에 방문 표시하고
    cnt += 1                            # 연결된 쓰레기의 수를 1 추가한다
    for t in range(4):                  # 4방향 탐색을 반복해서
        x = i + d[t][0]                 # x에 이동한 행을 저장하고
        y = j + d[t][1]                 # y에 이동한 열을 저장한다
        if 0<=x<N and 0<=y<M:           # x,y가 행렬 내에 위치하고
            if road[x][y] and visited[x][y] == 0:   # x,y에 쓰레기가 떨어져 있고 아직 방문 전이라면
                dfs(x, y)               # x,y 쓰레기와 연결된 쓰레기를 찾기위한 dfs 탐색을 한다

d = [[1,0],[-1,0],[0,1],[0,-1]]         # 4방향 탐색을 위한 리스트를 생성하고
ans = 0                                 # 가장 큰 음식물의 크기를 저장할 변수를 생성한다
for i in range(N):                      # 행을 반복하고
    for j in range(M):                  # 열을 반복해서
        cnt = 0                         # i,j와 연결된 쓰레기의 크기를 저장하기 위한 변수를 생성하고
        if road[i][j] and visited[i][j] == 0:       # i,j에 쓰레기가 떨어져 있고 아직 방문 전이라면
            dfs(i, j)                   # i,j 쓰레기와 연결된 쓰레기를 찾기위한 dfs 탐색을 한다
            ans = max(ans, cnt)         # ans와 cnt중 더 큰 음식물을 ans에 저장한다
print(ans)                              # 음식물 중 가장 큰 음식물의 크기를 출력한다