# 점프_BOJ1890

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                            # 게임판의 크기를 input 받고
jido = [list(map(int, input().split())) for _ in range(N)]  # 게임판에 적힌 숫자를 input 받은 후
dp = [[0]*N for _ in range(N)]                              # 정답을 저장할 dp를 생성한다
dp[0][0] = 1                                                # 출발점의 경우의수 1을 저장하고
for i in range(N):                                          # 행을 반복하고
    for j in range(N):                                      # 열을 반복해서
        if [i, j] == [N-1, N-1]:                            # 마지막점에 도착했다면
            break                                           # break한다
        tmp = jido[i][j]                                    # 현재 위치에서 점프할 수 있는 거리를 tmp에 저장하고
        if i + tmp < N:                                     # 아래쪽으로 점프 했을 때 게임판 안에 있다면
            dp[i+tmp][j] += dp[i][j]                        # 점프한 위치에 현재칸의 경우의 수를 더한다
        if j + tmp < N:                                     # 오른쪽으로 점프 했을 때 게임판 안에 있다면
            dp[i][j+tmp] += dp[i][j]                        # 점프한 위치에 현재칸의 경우의 수를 더한다
print(dp[N-1][N-1])                                         # 도착점의 경우의 수를 출력한다