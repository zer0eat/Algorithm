# 미세먼지 안녕!_BOJ17144

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
R, C, T = map(int, input().split())                                 # R 집의 행의 길이 / C 집의 열의 길이 / T 경과한 시간을 input받고
jido = [list(map(int, input().split())) for _ in range(R)]          # 집에 있는 미세먼지의 정보를 input 받는다
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]                              # 미세먼지가 확산하기 위해 사용할 델타탐색 리스트를 생성한다

# 공기청정기 위치 확인
air = []                                                            # 공기청정기의 위치를 저장할 리스트를 생성하고
for i in range(R):                                                  # 행을 반복해서
    if jido[i][0] == -1:                                            # 미세먼지 정보 중 -1인 부분이 나온다면
        air.append([i,0])                                           # 해당 위치를 공기청정기의 위치로 리스트에 append한다

# 미세먼지의 확산
def diffusion(jido):
    new = [[0]*C for _ in range(R)]                                 # 확산 후 미세먼지 정보를 저장할 리스트를 생성하고
    for r in range(R):                                              # 행을 반복하고
        for c in range(C):                                          # 열을 반복해서
            if jido[r][c] == -1:                                    # 해당 위치에 공기청정기가 있다면
                new[r][c] = -1                                      # new에도 공기청정기 표시를 한다
            elif jido[r][c] != 0:                                   # 해당 위치에 먼지가 있다면
                tmp = 0                                             # 확산한 방향의 수를 저장할 변수를 생성하고
                for t in range(4):                                  # 4방향 델타탐색을 반복해서
                    x = r + d[t][0]                                 # 이동한 위치의 행을 x에 저장하고
                    y = c + d[t][1]                                 # 이동한 위치의 열을 y에 저장해서
                    if 0<=x<R and 0<=y<C and [x,y] not in air:      # x,y가 방 안에 위치하고 공기청정기가 있는 위치가 아니라면
                        new[x][y] += jido[r][c]//5                  # x,y에 확산한 미세먼지를 더해주고
                        tmp += 1                                    # 확산한 방향의 수를 1 추가한다
                else:                                               # 4방향 탐색을 마쳤다면
                    new[r][c] += jido[r][c]                         # 확산 전 위치에 미세먼지를 더해주고
                    new[r][c] -= jido[r][c]//5*tmp                  # 확산한 만큼 미세먼지의 수를 빼준다
    return new                                                      # 확산 후 지도를 return한다

# 공기청정기 작동
def airfilter(jido):
    # 반시계 방향으로 순환
    for a in range(air[0][0]-1, 0, -1):                             # 반시계 방향으로 회전하는 순환에서 왼쪽 변을 반복해서
        jido[a][0] = jido[a-1][0]                                   # 한 행 위의 먼지 정보를 해당 칸에 저장한다
    for b in range(C-1):                                            # 반시계 방향으로 회전하는 순환에서 위쪽 변을 반복해서
        jido[0][b] = jido[0][b+1]                                   # 한 열 다음의 먼지 정보를 해당 칸에 저장한다
    for c in range(air[0][0]):                                      # 반시계 방향으로 회전하는 순환에서 오른쪽 변을 반복해서
        jido[c][C-1] = jido[c+1][C-1]                               # 한 행 아래의 먼지 정보를 해당 칸에 저장한다
    for d in range(C-1, 0, -1):                                     # 반시계 방향으로 회전하는 순환에서 아래쪽 변을 반복해서
        if d == 1:                                                  # 공기 청정기 바로 앞 칸이라면
            jido[air[0][0]][d] = 0                                  # 미세먼지를 0으로 저장하고
        else:                                                       # 바로 앞 칸이 아니라면
            jido[air[0][0]][d] = jido[air[0][0]][d-1]               # 한 열 이전의 먼지 정보를 해당칸에 저장한다
    # 시계 방향으로 순환
    for a in range(air[1][0]+1, R-1):                               # 시계 방향으로 회전하는 순환에서 왼쪽 변을 반복해서
        jido[a][0] = jido[a+1][0]                                   # 한 행 아래의 먼지 정보를 해당 칸에 저장한다
    for b in range(C-1):                                            # 시계 방향으로 회전하는 순환에서 아래쪽 변을 반복해서
        jido[R-1][b] = jido[R-1][b+1]                               # 한 열 이전의 먼지 정보를 해당 칸에 저장한다
    for c in range(R-1, air[1][0]-1, -1):                           # 시계 방향으로 회전하는 순환에서 오른쪽 변을 반복해서
        jido[c][C-1] = jido[c-1][C-1]                               # 한 행 위의 먼지 정보를 해당 칸에 저장한다
    for d in range(C-1, 0, -1):                                     # 시계 방향으로 회전하는 순환에서 위쪽 변을 반복해서
        if d == 1:                                                  # 공기 청정기 바로 앞 칸이라면
            jido[air[1][0]][d] = 0                                  # 미세먼지를 0으로 저장하고
        else:                                                       # 바로 앞 칸이 아니라면
            jido[air[1][0]][d] = jido[air[1][0]][d-1]               # 한 열 다음의 먼지 정보를 해당칸에 저장한다
    return jido                                                     # 확산 후 지도를 return한다

for t in range(T):                                                  # 경과된 시간의 수를 반복해서
    jido = diffusion(jido)                                          # 확산된 미세먼지를 jido에 업데이트하고
    jido = airfilter(jido)                                          # 공기청정기 작동 후 미세먼지를 jido에 업데이트한다
ans = 2                                                             # 미세먼지의 수를 저장할 변수를 생성하고
for i in range(R):                                                  # 방의 행을 크기를 반복해서
    ans += sum(jido[i])                                             # 한 행의 미세먼지의 합을 ans에 더한 후
print(ans)                                                          # T초 후 방에 남아있는 미세먼지의 양을 출력한다