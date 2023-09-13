# 안전영역_BOJ2468

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100001)

# input 받기
N = int(input())                                                # 지도의 길이를 input 받고
jido = []                                                       # 지도를 저장할 리스트를 생성한다
height = 0                                                      # 지도의 최대 높이를 저장할 변수를 생성하고
for _ in range(N):                                              # 지도의 행을 반복해서
    A = list(map(int, input().split()))                         # 지도의 한 행을 리스트로 input받고
    jido.append(A)                                              # jido 리스트에 append하고
    height = max(height, max(A))                                # 최대 높이를 height에 저장한다

d = [[1,0],[-1,0],[0,1],[0,-1]]                                 # 하상우좌 이동할 리스트를 생성하고
def dfs(i, j):
    global N                                                    # N을 global로 선언한다
    if visited[i][j] == 0:                                      # i, j가 방문 전이라면
        visited[i][j] = 1                                       # 방문표시를 하고
        for t in range(4):                                      # 4방향을 반복해서
            x = i + d[t][0]                                     # 이동한 위치의 행을 x에 저장하고
            y = j + d[t][1]                                     # 이동한 위치의 열을 y에 저장한다
            if 0<=x<N and 0<=y<N and visited[x][y] == 0:        # x,y가 jido 내에 위치하면서 x,y가 방문 전이라면
                dfs(x, y)                                       # x,y를 넣어 dfs 탐색을 한다

ans = 1                                                         # 섬의 개수를 저장할 변수를 생성하고
for n in range(1, height):                                      # 강우량을 1부터 최대 높이까지 반복해서
    visited = [[0]*N for _ in range(N)]                         # 방문표시를 할 리스트를 생성하고
    for i in range(N):                                          # 행을 반복하고
        for j in range(N):                                      # 열을 반복해서
            if jido[i][j] <= n:                                 # i, j가 강우량보다 같거나 낮다면
                visited[i][j] = 1                               # 방문표시를 한다
    tmp = 0                                                     # 현재 강우량에 안전구역의 개수를 저장할 변수를 생성하고
    for i in range(N):                                          # 행을 반복하고
        for j in range(N):                                      # 열을 반복해서
            if visited[i][j] == 0:                              # 아직 방문 전이라면
                dfs(i,j)                                        # i, j를 dfs 탐색을 한다
                tmp += 1                                        # 안전구역의 수를 1 추가하고
    else:                                                       # 모든 지도를 탐색했다면
        ans = max(ans, tmp)                                     # ans에 가장 많은 안전구역을 저장한다
print(ans)                                                      # 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다