# 지뢰찾기_BOJ1996

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                # 지뢰 맵의 크기를 input 받고
mine = [list(input().strip()) for _ in range(N)]                # 지뢰가 깔린 정보를 행렬로 input 받는다
d = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]     # 8방향으로 델타 탐색하기 이동하기 위한 리스트를 생성하고
ans = [[0]*N for _ in range(N)]                                 # 정답을 저장할 행렬을 생성한다
for i in range(N):                                              # 행을 반복하고
    for j in range(N):                                          # 열을 반복해서
        if mine[i][j] == '.':                                   # 해당 위치에 지뢰가 없다면
            tmp = 0                                             # 주변 지뢰의 수를 저장할 변수를 생성하고
            for k in range(8):                                  # 8방향 탐색을 진행해서
                x = i + d[k][0]                                 # 이동한 행을 x에 저장하고
                y = j + d[k][1]                                 # 이동한 열을 y에 저장해서
                if 0<=x<N and 0<=y<N:                           # 이동한 행렬이 맵 안에 있는 경우
                    if mine[x][y] != '.':                       # 이동한 위치에 .이 아니고 지뢰가 있다면
                        tmp += int(mine[x][y])                  # 지뢰의 수를 tmp에 더해준다
            else:                                               # 8방향 탐색을 모두 마친 후
                if tmp > 9:                                     # tmp의 수가 9보다 크다면
                    tmp = 'M'                                   # tmp를 M으로 바꿔 저장하고
                ans[i][j] = tmp                                 # ans에 주위의 지뢰의 수를 tmp로 저장한다
        else:                                                   # 해당 위치에 지뢰가 있다면
            ans[i][j] = '*'                                     # ans에 *로 지뢰표시를 해준다
for i in range(N):                                              # 행을 반복하고
    for j in range(N):                                          # 열을 반복해서
        if j == N-1:                                            # 한 행의 마지막 원소인 경우
            print(ans[i][j])                                    # 원소를 출력하고 줄을 바꿔준다
        else:                                                   # 한 행의 마지막 원소가 아닌 경우
            print(ans[i][j], end='')                            # 원소를 붙여서 출력한다