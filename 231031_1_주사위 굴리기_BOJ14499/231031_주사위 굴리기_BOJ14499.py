# 주사위 굴리기_BOJ14499

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M, x, y, K = map(int, input().split())                   # N 지도의 행의 길이 / M 지도의 열의 길이 / x 주사위의 행의 위치 / y 주사위의 열의 위치 / K 주사위를 굴릴 횟수
jido = [list(map(int, input().split())) for _ in range(N)]  # 지도의 원소를 행렬로 input 받고
move = list(map(int, input().split()))                      # 주사위를 굴릴 방향을 리스트로 input 받는다

def rolling(m):
    if m == 1:                                              # 주사위를 동쪽으로 굴렸을 때
        dice[0], dice[1], dice[2], dice[3],dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5],dice[4], dice[2]
    elif m == 2:                                            # 주사위를 서쪽으로 굴렸을 때
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0],dice[4], dice[3]
    elif m == 3:                                            # 주사위를 북쪽으로 굴렸을 때
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3],dice[5], dice[1]
    else:                                                   # 주사위를 남쪽으로 굴렸을 때
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3],dice[0], dice[4]

dice = [0]*6                                                # 주사위의 숫자를 저장할 리스트를 생성하고(0 하늘 / 1 0기준 위 / 2 0기준 오른쪽 / 3 0기준 왼쪽 / 4 0기준 아래 / 5 바닥을 향함)
d = [[0, 1], [0, -1], [-1, 0], [1, 0]]                      # 주사위를 굴렸을 때 델타이동할 리스트를 생성한다
for m in move:                                              # 주사위를 굴리는 것을 반복해서
    r = x + d[m-1][0]                                       # 주사위를 굴렸을 때 행의 위치를 r에 저장하고
    c = y + d[m-1][1]                                       # 주사위를 굴렸을 때 열의 위치를 c에 저장한다
    if 0<=r<N and 0<=c<M:                                   # 이동한 위치가 지도 내에 있다면
        x, y = r, c                                         # x,y에 r,c를 각각 저장하고
        rolling(m)                                          # 주사위를 해당 방향으로 굴렸을 때 리스트를 정렬한 후
        print(dice[0])                                      # 하늘을 바라보는 면을 출력한다
        if jido[x][y] != 0:                                 # 지도의 칸이 0이 아니라면
            dice[5] = jido[x][y]                            # 다이스의 바닥면에 지도의 숫자를 저장하고
            jido[x][y] = 0                                  # 지도의 숫자를 0으로 저장한다
        else:                                               # 지도의 칸이 0이 이라면
            jido[x][y] = dice[5]                            # 지도의 칸에 다이스의 바닥면의 숫자를 저장한다