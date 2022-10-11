# 적록색약_BOJ10026

# input.txt 열기
import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(2500)                                         # 재귀의 깊이를 2500까지 늘려주고

def normal(i, j, colornormal):                                      # normal함수를 돌려서
    for k in range(4):                                              # 상우하좌 방향으로 델타 탐색을 한후
        if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N:               # 행렬의 범위 안에서
            if arr[i + dx[k]][j + dy[k]] == colornormal and visitednormal[i + dx[k]][j + dy[k]] == 0:   # 같은 색상이면서 방문하지 않았다면
                visitednormal[i + dx[k]][j + dy[k]] = 1             # 방문처리하고
                normal(i + dx[k], j + dy[k], colornormal)           # 해당지점에서 다시 normal 함수를 통해 인접한 색상을 찾는다

def RG(i, j, colorRG):                                              # RG함수를 돌려서
    for k in range(4):                                              # 상우하좌 방향으로 델타 탐색을 한후
        if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N:               # 행렬의 범위 안에서
            if arr[i + dx[k]][j + dy[k]] in colorRG and visitedRG[i + dx[k]][j + dy[k]] == 0:           # colorRG에 속한 색상이면서 방문하지 않았다면
                visitedRG[i + dx[k]][j + dy[k]] = 1                 # 방문처리하고
                RG(i + dx[k], j + dy[k], colorRG)                   # 해당지점에서 다시 RG 함수를 통해 인접한 색상을 찾는다

# input 받기
N = int(sys.stdin.readline())                                       # N 정사각형 행렬의 한변의 길이
arr = [list((sys.stdin.readline().rstrip())) for n in range(N)]     # N열의 N행의 행렬을 arr에 input 받음

visitednormal = [[0]*N for n in range(N)]                           # 정상을 체크할 visited리스트 생성
visitedRG = [[0]*N for n in range(N)]                               # 적록색약을 체크할 visited리스트 생성

dx = [-1, 0, 1, 0]                                                  # 상우하좌 순서대로 행이동하는 델타탐색
dy = [0, 1, 0, -1]                                                  # 상우하좌 순서대로 열이동하는 델타탐색
cntNormal = 0                                                       # 정상의 구역의 개수를 셀 cnt
cntRG = 0                                                           # 적록색약의 구역의 개수를 셀 cnt

for i in range(N):                                                  # 행을 반복하고
    for j in range(N):                                              # 열을 반복해서
        if visitednormal[i][j] == 0:                                # 방문하지 않은점을 도착했을 때(normal)
            visitednormal[i][j] == 1                                # 방문으로 표시하고
            colornormal = arr[i][j]                                 # 해당 지점의 색을 colornormal에 복사한다
            normal(i, j, colornormal)                               # normal함수에 해당지점부터 넣어 인접한 같은 색상을 모두 방문처리한다
            cntNormal += 1                                          # 구역을 세는 변수에 숫자를 1 추가한다

        if visitedRG[i][j] == 0:                                    # 방문하지 않은점을 도착했을 때(RG)
            visitedRG[i][j] == 1                                    # 방문으로 표시하고
            if arr[i][j] == 'R' or arr[i][j] == 'G':                # 해당 지점의 색이 R or G라면
                colorRG = ['R', 'G']                                # colorRG 에 리스트로 ['R', 'G']를 저장한다
            elif arr[i][j] == 'B':                                  # 해당 지점의 색이 B라면
                colorRG = ['B']                                     # colorRG 에 리스트로 ['B']를 저장한다
            RG(i, j, colorRG)                                       # RG함수에 해당지점부터 넣어 인접한 같은 색상을 모두 방문처리한다
            cntRG += 1                                              # 구역을 세는 변수에 숫자를 1 추가한다
print(cntNormal, cntRG)