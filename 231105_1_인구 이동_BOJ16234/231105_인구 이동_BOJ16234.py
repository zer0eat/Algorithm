# 인구 이동_BOJ16234

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# input 받기
N, L, R = map(int, input().split())                         # N 땅의 크기 / L 두 나라간 인구차이의 최소값 / R 두 나라간 인구차이의 최대값을 input 받고
earth = [list(map(int, input().split())) for _ in range(N)] # 나라의 인구정보를 input 받아 행렬로 저장하고
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]                      # 4방향 델타이동할 리스트를 생성한다

def union(r, c):
    global L, R                                             # 인구차의 최소값과 최대값을 global 변수로 선언하고
    visited[r][c] = 1                                       # r,c의 나라를 방문표시하고
    tmp.append([r, c])                                      # 이동할 나라 리스트에 append한다
    for t in range(4):                                      # 4방향 반복을 반복해서
        x = r + d[t][0]                                     # x에 이동한 위치의 행을 저장하고
        y = c + d[t][1]                                     # y에 이동한 위치의 열을 저장한다
        if 0<=x<N and 0<=y<N and visited[x][y] == 0:        # 이동한 위치가 땅 내에 존재하고 방문 전이라면
            people = abs(earth[r][c] - earth[x][y])         # people에 이동 전후의 인구수 차이를 저장하고
            if people >= L and people <= R:                 # 인구수 차이가 L이상 R 이하라면
                union(x, y)                                 # 이동한 위치를 union을 통해 이동할 나라를 탐색한다

def move(lst):
    tmp = 0                                                 # 인구수를 저장할 변수를 생성하고
    for l in lst:                                           # 나라 리스트를 반복해서
        tmp += earth[l[0]][l[1]]                            # tmp에 해당 나라의 인구수를 더하고
    else:                                                   # 리스트 내 나라의 인구수를 모두 더한 후
        tmp = int(tmp/len(lst))                             # 인구이동을 하여 리스트 내 나라의 평균 인구를 구하고
        for l in lst:                                       # 나라 리스트를 반복해서
            earth[l[0]][l[1]] = tmp                         # 이동 후 인구수를 저장한다

cnt = 0                                                     # 인구이동 횟수를 저장할 변수를 생성하고
while 1:                                                    # break가 나올때까지 반복해서
    visited = [[0]*N for _ in range(N)]                     # 방문표시를 할 리스트를 생성한다
    movement = []                                           # 인구이동을 할 나라를 저장할 리스트를 생성하고
    for i in range(N):                                      # 행을 반복하고
        for j in range(N):                                  # 열을 반복해서
            tmp = []                                        # 인구이동을 할 나라를 저장할 리스트를 생성하고
            if visited[i][j] == 0:                          # 방문하지 않은 나라가 나왔다면
                union(i, j)                                 # union을 통해 이동할 나라를 탐색한다
            if len(tmp) > 1:                                # 인구이동할 나라가 1개가 아니라면
                movement.append(tmp)                        # 인구이동을 할 리스트를 append한다
    if movement:                                            # 인구이동을 할 나라가 있다면
        for a in movement:                                  # 인구이동을 할 리스트를 반복해서
            move(a)                                         # move를 통해 a 안에 있는 나라간 이동을 수행하고
        cnt += 1                                            # 모든 인구이동을 마친 후 이동 횟수를 1 추가한다
    else:                                                   # 인구이동을 할 나라가 없다면
        break                                               # while문을 break한다
print(cnt)                                                  # 인구이동이 발생한 횟수를 출력한다