# 로봇 청소기_BOJ14503

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                            # N 방의 행의 길이 / M 방의 열의 길이를 input 받고
x, y, q = map(int, input().split())                         # 로봇청소기의 위치 x,y와 로봇청소기의 방향 q를 input 받고
room = [list(map(int, input().split())) for _ in range(N)]  # 방의 정보를 행렬로 input 받는다
d = [[-1,0], [0,1], [1,0], [0,-1]]                          # 로봇청소기가 바라보는 방향을 북 동 남 서로 생성한다

def clean(r, c, direction):
    global ans                                              # 청소한 방의 수를 저장할 변수를 global로 선언하고
    # 현재 칸 청소하기
    if room[r][c] == 0:                                     # 로봇 청소기의 현재위치가 청소 전이라면
        ans += 1                                            # 청소한 방의 수를 1 추가하고
        room[r][c] = 2                                      # 청소 표시를 한다
    # 4방향 청소가 다 안된 경우
    for i in range(1,5):                                    # 반시계 방향으로 돌며 4방향을 반복해서
        if direction - i < 0:                               # 현재 방향에서 반시계로 이동시 음수가 된다면
            h = direction - i + 4                           # 반시계로 이동 후 4를 더한 방향을 h에 저장하고
        else:                                               # 현재 방향에서 반시계로 이동해도 음수가 아니라면
            h = direction - i                               # 반시계로 이동한 방향을 h에 저장한다
        x = r + d[h][0]                                     # 이동한 방향의 행의 x에 저장하고
        y = c + d[h][1]                                     # 이동한 방향의 열을 y에 저장해서
        if 0<=x<N and 0<=y<M:                               # 이동한 위치가 방 안에 위치한다면
            if room[x][y] == 0:                             # 이동한 위치가 청소 전일 경우에
                clean(x, y, h)                              # clean에 해당 위치와 방향을 넣고 이동하여 청소하고
                return                                      # return한다
    # 4방향 청소가 다 된 경우
    else:                                                   # 4방향 모두 청소할 곳이 없는 경우에는
        h = (direction + 2) % 4                             # 현재 바라보는 방향에서 후진을 하기위한 방향을 h에 저장하고
        x = r + d[h][0]                                     # 후진한 곳의 행을 x에 저장하고
        y = c + d[h][1]                                     # 후진한 곳의 열을 y에 저장해서
        if 0<=x<N and 0<=y<M:                               # 이동한 위치가 방 안에 위치한다면
            if room[x][y] != 1:                             # 이동한 위치가 벽이 아닐 경우에
                clean(x, y, direction)                      # clean에 해당 위치와 방향을 넣고 이동하고
                return                                      # return한다

ans = 0                                                     # 청소한 방의 수를 저장할 변수를 생성하고
clean(x, y, q)                                              # 로봇청소기의 시작점과 방향을 clean함수에 넣어 방청소를 시작한 후
print(ans)                                                  # 청소한 방의 넓이를 출력한다