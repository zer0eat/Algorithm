# 그림_BOJ1926

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(250001)

# input 받기
N, M = map(int, input().split())                                # N 행의크기 / M 열의크기를 input받고
paper = [list(map(int, input().split())) for _ in range(N)]     # 그림이 그려진 도화지를 input 받고
visited = [[0]*M for _ in range(N)]                             # 방문표시를 할 행령을 생성한다

def dfs(i, j):
    global tmp                                                  # tmp를 global 변수로 선언하고
    visited[i][j] = 1                                           # i,j를 방문 표시한다
    tmp += 1                                                    # 그림의 크기를 1 추가하고
    for t in range(4):                                          # 4방향 탐색을 반복해서
        x = i + d[t][0]                                         # 이동한 곳의 행을 저장하고
        y = j + d[t][1]                                         # 이동한 곳의 열을 저장해서
        if 0<=x<N and 0<=y<M:                                   # 이동한 곳이 도화지 내에 있으면
            if paper[x][y] == 1 and visited[x][y] == 0:         # 해당위치에 그림이 있고 방문 전이라면
                dfs(x,y)                                        # dfs 탐색을 한다

cnt = 0                                                         # 그림의 개수를 저장할 변수를 생성하고
ans = 0                                                         # 그림의 최대 크기를 저장할 변수를 생성한다
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]                          # 4방향 이동을 할 리스트를 생성하고
for i in range(N):                                              # 행을 반복하고
    for j in range(M):                                          # 열을 반복해서
        if paper[i][j] == 1 and visited[i][j] == 0:             # 해당위치에 그림이 있고 방문 전이라면
            cnt += 1                                            # 그림의 수를 1 추가하고
            tmp = 0                                             # 그림의 크기를 저장할 변수를 생성한 후
            dfs(i, j)                                           # dfs 탐색한다
            ans = max(ans, tmp)                                 # tmp와 ans 중 크기가 큰 그림을 ans에 저장한다 
print(cnt)                                                      # 그림의 개수를 출력하고
print(ans)                                                      # 가장 큰 그림의 크기를 출력한다