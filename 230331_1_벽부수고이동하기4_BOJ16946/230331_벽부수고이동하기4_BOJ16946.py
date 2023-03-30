# 벽부수고이동하기4_BOJ16946

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(1000001)
import copy

# input 받기
N, M = map(int, input().split())                            # N 행의길이 / M 열의길이
RC = [list(map(int, input().strip())) for _ in range(N)]    # RC 행렬로 표시된 맵을 input 받고
zero = [[0]*M for _ in range(N)]                            # 맵에서 0으로 표시된 부분중 연결된 부분을 세서 저장할 행렬을 생성

dx = [-1,0,1,0]                                             # 상, 우, 하, 좌로 네방향 탐색을 할 행의 이동 리스트 생성
dy = [0,1,0,-1]                                             # 상, 우, 하, 좌로 네방향 탐색을 할 열의 이동 리스트 생성

def dfs(x,y):
    for z in range(4):                                      # 네방향을 반복해서
        if 0 <= x+dx[z] < N and 0 <= y+dy[z] < M:           # 이동 위치가 행렬 내에 있을 때
            if visited[x+dx[z]][y+dy[z]] == 0:              # 이동위치가 0이라면
                visited[x+dx[z]][y+dy[z]] = 1               # 해당 위치를 1로 바꾸고
                jido.append([x+dx[z],y+dy[z]])              # jido 리스트에 이동한 위치를 리스트에 담아 append
                dfs(x+dx[z], y+dy[z])                       # 이동한 위치를 dfs에 넣고 다시 탐색
    return                                                  # for문을 모두 반복했다면 return한다

visited = copy.deepcopy(RC)                                 # RC 행렬을 visited에 복사한 후

tag = 1                                                     # 0의 집단이 몇번째인지 셀 변수 생성
for i in range(N):                                          # 행을 반복해고
    for j in range(M):                                      # 열을 반복해서
        if visited[i][j] == 0:                              # visited 행렬에서 해당 위치가 0이라면
            visited[i][j] = 1                               # 해당 위치를 1로 바꾸고
            jido = [[i,j]]                                  # 해당 위치를 jido에 넣은 리스트를 생성
            dfs(i,j)                                        # 해당 위치부터 dfs 탐색을 진행해서
            tmp = len(jido)                                 # 이어진 0의 개수를 tmp에 저장하고
            for x, y in jido:                               # jido에 담긴 위치를 반복해서
                zero[x][y] = [tmp, tag]                     # zero 행렬에 해당 위치에 [연결된 0의수, 0의 집단의 순서]로 저장한다
            tag += 1                                        # 집단 번호를 1 증가 시킨다

for i in range(N):                                          # 행을 반복하고
    for j in range(M):                                      # 열을 반복해서
        if RC[i][j] == 1:                                   # RC 행렬에서 해당 위치가 1이라면
            tmp = 1                                         # 이동할 수 있는 위치를 저장할 변수를 생성하고
            tag = dict()                                    # 집단을 저장할 tag라는 딕셔너리를 생성한다
            for z in range(4):                              # 네방향 탐색을 반복해서
                if 0 <= i+dx[z] < N and 0 <= j+dy[z] < M:   # 이동한 곳이 행렬 내에 있다면
                    if zero[i+dx[z]][j+dy[z]] != 0 and tag.get(zero[i+dx[z]][j+dy[z]][1]) == None:  # 이동한 곳이 zero행렬에서 0이 아니면서 딕셔너리에 해당 집단이 포함되지 않았다면
                        tmp += zero[i+dx[z]][j+dy[z]][0]    # tmp에 이어진 0의 수를 더해주고
                        tag[zero[i+dx[z]][j+dy[z]][1]] = 1  # 이어진 0의 집단을 tag에 넣어 방문표시를 한다
            else:                                           # 4방향 탐색을 끝냈다면
                RC[i][j] = (tmp%10)                         # RC의 해당위치에 tmp의 일의자리 숫자만 저장한다
else:                                                       # 행렬의 모든 원소의 탐색을 마쳤다면
    for i in range(N):                                      # 행을 반복하고
        tmp = ''                                            # 정답을 출력할 빈 문자열 변수를 생성하고
        for j in range(M):                                  # 열을 반복해서
            tmp += str(RC[i][j])                            # 해당위치의 숫자를 문자열 형태로 tmp에 더한 후
        else:                                               # 한 행의 모든 열을 확인했다면
            print(tmp)                                      # 저장된 tmp를 출력한다