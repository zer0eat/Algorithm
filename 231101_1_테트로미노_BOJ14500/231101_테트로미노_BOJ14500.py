# 테트로미노_BOJ14500

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                            # N 종이의 행의 크기 / M 종이의 열의 크기를 input 받고
paper = [list(map(int, input().split())) for _ in range(N)] # 종이에 있는 수의 정보를 행렬로 input받고
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]                      # 4방향으로 델타이동할 리스트를 생성하고
visited = [[0]*M for _ in range(N)]                         # 방문표시를 할 리스트를 생성한다

def dfs(i, j, cnt, tetromino):
    global ans                                              # 테트로미노의 최댓값을 저장할 ans를 global로 선언하고
    tetromino += paper[i][j]                                # i,j에 해당하는 숫자를 tetromino에 저장하고
    if cnt == 4:                                            # 테트로미노가 4칸이 완성되었다면
        ans = max(ans, tetromino)                           # 현재 저장된 수와 최댓값중 더 큰 값을 ans에 저장하고
        return                                              # return한다
    for t in range(4):                                      # 테트로미노가 완성되지 않은 경우 4방향 이동을 반복해서
        x = i + d[t][0]                                     # x에 이동한 행의 위치를 저장하고
        y = j + d[t][1]                                     # y에 이동한 열의 위치를 저장해서
        if 0<=x<N and 0<=y<M and visited[x][y] == 0:        # 이동한 위치가 종이 위에 있고 방문 전이라면
            visited[x][y] = 1                               # 이동한 위치를 방문표시하고
            dfs(x, y, cnt+1, tetromino)                     # dfs 탐색한 후
            visited[x][y] = 0                               # 이동한 위치를 방문표시 해제한다

def oh(i,j):
    global N, M, ans                                        # 행렬의 크기 N, M과 테트로미노의 최댓값을 저장할 ans를 global로 선언하고
    if (i == 0 or i == N-1) and (j == 0 or j == M-1):       # i,j의 위치가 종이의 모서리라면
        return                                              # return한다
    elif i == 0:                                            # i,j의 위치가 종이의 맨 윗줄이라면
        tetromino = paper[i][j]                             # tetromino에 i,j의 숫자를 저장하고
        for t in range(4):                                  # i,j를 기준으로 상우하좌를 반복해서
            if t != 0:                                      # 위쪽을 제외하고
                x = i + d[t][0]                             # x에 이동한 행의 위치를 저장하고
                y = j + d[t][1]                             # y에 이동한 열의 위치를 저장해서
                tetromino += paper[x][y]                    # 이동한 위치의 숫자를 tetromino에 더하고
        ans = max(ans, tetromino)                           # 현재 저장된 수와 최댓값중 더 큰 값을 ans에 저장한다
    elif j == M-1:                                          # i,j의 위치가 종이의 맨 오른쪽 줄이라면
        tetromino = paper[i][j]                             # tetromino에 i,j의 숫자를 저장하고
        for t in range(4):                                  # i,j를 기준으로 상우하좌를 반복해서
            if t != 1:                                      # 오른쪽을 제외하고
                x = i + d[t][0]                             # x에 이동한 행의 위치를 저장하고
                y = j + d[t][1]                             # y에 이동한 열의 위치를 저장해서
                tetromino += paper[x][y]                    # 이동한 위치의 숫자를 tetromino에 더하고
        ans = max(ans, tetromino)                           # 현재 저장된 수와 최댓값중 더 큰 값을 ans에 저장한다
    elif i == N-1:                                          # i,j의 위치가 종이의 맨 아래 줄이라면
        tetromino = paper[i][j]                             # tetromino에 i,j의 숫자를 저장하고
        for t in range(4):                                  # i,j를 기준으로 상우하좌를 반복해서
            if t != 2:                                      # 아래쪽을 제외하고
                x = i + d[t][0]                             # x에 이동한 행의 위치를 저장하고
                y = j + d[t][1]                             # y에 이동한 열의 위치를 저장해서
                tetromino += paper[x][y]                    # 이동한 위치의 숫자를 tetromino에 더하고
        ans = max(ans, tetromino)                           # 현재 저장된 수와 최댓값중 더 큰 값을 ans에 저장한다
    elif j == 0:                                            # i,j의 위치가 종이의 맨 왼쪽 줄이라면
        tetromino = paper[i][j]                             # tetromino에 i,j의 숫자를 저장하고
        for t in range(4):                                  # i,j를 기준으로 상우하좌를 반복해서
            if t != 3:                                      # 왼쪽을 제외하고
                x = i + d[t][0]                             # x에 이동한 행의 위치를 저장하고
                y = j + d[t][1]                             # y에 이동한 열의 위치를 저장해서
                tetromino += paper[x][y]                    # 이동한 위치의 숫자를 tetromino에 더하고
        ans = max(ans, tetromino)                           # 현재 저장된 수와 최댓값중 더 큰 값을 ans에 저장한다
    else:                                                   # 종이의 가장자리가 아니라면
        tetromino = paper[i][j]                             # tetromino에 i,j의 숫자를 저장하고
        for t in range(4):                                  # i,j를 기준으로 상우하좌를 반복해서
            x = i + d[t][0]                                 # x에 이동한 행의 위치를 저장하고
            y = j + d[t][1]                                 # y에 이동한 열의 위치를 저장해서
            tetromino += paper[x][y]                        # 이동한 위치의 숫자를 tetromino에 더하고
        for t in range(4):                                  # i,j를 기준으로 상우하좌를 반복해서
            x = i + d[t][0]                                 # x에 이동한 행의 위치를 저장하고
            y = j + d[t][1]                                 # y에 이동한 열의 위치를 저장해서
            tetromino -= paper[x][y]                        # 이동한 위치의 숫자를 tetromino에 빼주고
            ans = max(ans, tetromino)                       # 현재 저장된 수와 최댓값중 더 큰 값을 ans에 저장하고
            tetromino += paper[x][y]                        # 이동한 위치의 숫자를 tetromino에 더해준다

ans = 0                                                     # 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 저장할 변수를 생성하고
for i in range(N):                                          # 행을 반복하고
    for j in range(M):                                      # 열을 반복해서
        visited[i][j] = 1                                   # i,j를 방문표시하고
        dfs(i, j, 1, 0)                                     # dfs 탐색하고
        visited[i][j] = 0                                   # i,j를 방문표시 해제하고
        oh(i, j)                                            # ㅗ 모양의 테트로미노를 탐색하고
print(ans)                                                  # 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다