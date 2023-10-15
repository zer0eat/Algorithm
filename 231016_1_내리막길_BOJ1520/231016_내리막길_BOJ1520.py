# 내리막길_BOJ1520

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
M, N = map(int, input().split())                            # M 행의 길이 / N 열의 길이를 input 받고
jido = [list(map(int, input().split())) for _ in range(M)]  # 높이정보를 행렬로 input 받는다
visited = [[-1]*N for _ in range(M)]                        # 방문표시를 할 행렬을 생성하고
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]                      # 4방향으로 델타이동할 리스트를 생성한다

def dfs(a, b):
    if a == M-1 and b == N-1:                               # 도착지에 도달했다면
        return 1                                            # 1을 return한다
    if visited[a][b] != -1:                                 # 방문한 경험이 있다면
        return visited[a][b]                                # 해당 위치의 경우의 수를 return한다
    else:                                                   # 방문한 경험이 없다면
        visited[a][b] = 0                                   # 방문표시를 하고
        for t in range(4):                                  # 4방향 탐색을 수행해서
            x = a + d[t][0]                                 # x에 이동한 행과
            y = b + d[t][1]                                 # y에 이동한 열을 저장한다
            if 0<=x<M and 0<=y<N:                           # x,y가 행렬 내에 존재하고
                if jido[a][b] > jido[x][y]:                 # 이동 전 높이가 이동 후 높이보다 높다면
                    visited[a][b] += dfs(x, y)              # 이동 후 위치를 dfs 함수로 탐색해서 이동 전 위치의 경우의 수에 더해준다
        return visited[a][b]                                # 4방향 탐색을 모두 진행한 후 a,b 위치의 경우의 수를 return 한다

print(dfs(0, 0))                                            # dfs 탐색을 통해 이동 가능한 경로의 수를 출력한다