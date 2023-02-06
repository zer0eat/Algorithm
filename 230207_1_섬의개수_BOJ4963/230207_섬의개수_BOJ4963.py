# 섬의개수_BOJ4963

# input.txt 열기
import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)

def DFS(i, j):
    jido[i][j] = 2                                                              # i, j 위치를 방문한 땅을 표시하기 위해 2로 바꾸고
    for z in range(8):                                                          # 8방향을 모두 반복해서
        if 0 <= i + dx[z] < h and 0 <= j + dy[z] < w:                           # 델타 탐색한 곳이 행과 열이 모두 지도 안이라면
            if jido[i + dx[z]][j + dy[z]] == 1:                                 # 해당 지역이 땅이였을 때
                DFS(i + dx[z], j + dy[z])                                       # 해당 지역을 DFS 함수로 탐색한다

# input 받기
dx = [-1, -1, 0, 1, 1, 1, 0, -1]                                                # 8방향 델타탐색 행(상,상우,우,우하,하,하좌,좌,상좌)
dy = [0, 1, 1, 1, 0, -1, -1, -1]                                                # 8방향 델타탐색 열(상,상우,우,우하,하,하좌,좌,상좌)

while 1:                                                                        # break가 나올 때까지 반복해서
    w, h = map(int, sys.stdin.readline().split())                               # w 열의 길이 / h 행의 길이
    if w == 0 and h == 0:                                                       # w, h 둘 다 0이면
        break                                                                   # while문 break
    jido = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]     # jido
    ans = 0                                                                     # 섬의 수를 저장할 변수 생성
    for i in range(h):                                                          # 행을 반복하고
        for j in range(w):                                                      # 열을 반복해서
            if jido[i][j] == 1:                                                 # i,j의 위치가 땅이라면
                ans += 1                                                        # ans에 1을 추가하고
                DFS(i, j)                                                       # i,j를 시작점으로 DFS 탐색하여 섬을 모두 표시한다
    print(ans)                                                                  # 모든 땅의 탐색을 마쳤다면 ans를 출력한다

