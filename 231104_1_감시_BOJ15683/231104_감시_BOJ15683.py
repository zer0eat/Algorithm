# 감시_BOJ15683

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import copy

# input 받기
N, M = map(int, input().split())                                # N 사무실의 행의 길이 / M 사무실의 열의 길이를 input 받고
office = [list(map(int, input().split())) for _ in range(N)]    # 사무실의 cctv와 벽의 위치 정보를 행렬로 input 받는다
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]                          # 4방향 델타 이동할 리스틀르 생성하고
type_cctv = [[],                                                # cctv의 타입에 따른 관찰 방향을 저장한 리스트를 생성해서
             [[0], [1], [2], [3]],                              # 1번 cctv일 때 관찰할 방향
             [[0, 2], [1, 3]],                                  # 2번 cctv일 때 관찰할 방향
             [[0, 1], [1, 2], [2, 3], [0, 3]],                  # 3번 cctv일 때 관찰할 방향
             [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],      # 4번 cctv일 때 관찰할 방향
             [[0, 1, 2, 3]]]                                    # 5번 cctv일 때 관찰할 방향을 넣고 리스트를 생성한다
cctv = []                                                       # cctv의 위치를 저장할 리스트를 생성해서
for i in range(N):                                              # 행을 반복하고
    for j in range(M):                                          # 열을 반복해서
        if office[i][j] != 0 and office[i][j] != 6:             # cctv가 있고 벽이 아니라면
            cctv.append([i, j, office[i][j]])                   # cctv에 위치와 cctv 종류를 append한다

def find(r, c, dir, new_office):
    for a in dir:                                               # cctv의 방향을 반복해서
        x = r                                                   # cctv의 위치의 행을 x에 저장하고
        y = c                                                   # cctv의 위치의 열을 y에 저장한다
        while 1:                                                # break가 나올때까지 반복해서
            x += d[a][0]                                        # x에 a방향으로 이동한 값을 저장하고
            y += d[a][1]                                        # y에 a방향으로 이동한 값을 저장해서
            if 0<=x<N and 0<=y<M:                               # 이동한 곳이 사무실내에 있고
                if new_office[x][y] == 6:                       # 이동한 곳이 벽이라면
                    break                                       # while문을 break하고
                elif new_office[x][y] == 0:                     # 이동한 곳이 빈공간이라면
                    new_office[x][y] = -1                       # 감시 표시를 한다
            else:                                               # 이동한 곳이 사무실 밖에 있다면
                break                                           # while문을 break한다

def dfs(idx, office):
    global ans                                                  # ans를 global 변수로 선언하고
    if idx == len(cctv):                                        # idx가 cctv의 개수와 같다면
        tmp = 0                                                 # 사각지대의 수를 셀 변수를 생성하고
        for i in range(N):                                      # 행을 반복하고
            for j in range(M):                                  # 열을 반복해서
                if office[i][j] == 0:                           # 사각지대라면
                    tmp += 1                                    # tmp에 1 추가한다
        ans = min(ans, tmp)                                     # ans와 tmp중 사각지대가 더 적은 값을 ans에 저장하고
        return                                                  # return한다
    r, c, t = cctv[idx]                                         # idx인덱스의 cctv의 행 열 cctv 타입을 저장하고
    new_office = copy.deepcopy(office)                          # 현재 office를 deepcopy해서
    for i in type_cctv[t]:                                      # cctv의 타입에 따른 관찰 방향을 반복해서
        find(r, c, i, new_office)                               # find함수로 관찰지대를 찾고
        dfs(idx + 1, new_office)                                # dfs로 다음 cctv 감시 범위를 탐색하고
        new_office = copy.deepcopy(office)                      # new_office를 office로 deepcopy해서

idx = 0                                                         # cctv의 개수를 셀 인덱스를 생성하고
ans = N * M                                                     # 사각지대의 최소값을 저장할 변수를 생성한다
dfs(0, office)                                                  # dfs 함수를 통해 cctv의 감시 범위를 탐색해서
print(ans)                                                      # 사각 지대의 최소 크기를 출력한다