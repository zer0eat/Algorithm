# Hoof, Paper, Scissors (Silver)_BOJ14453

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 가위바위보를 할 횟수를 input 받고
HPS = [input().strip() for _ in range(N)]   # 가위바위보를 낸 정보를 리스트로 input 받는다
dp = [[0]*N for _ in range(3)]              # 낸 횟수를 저장할 리스트를 생성하고
for h in range(N):                          # 가위바위보 횟수를 반복해서
    if HPS[h] == 'P':                       # h번째 보자기를 냈다면
        dp[0][h] = dp[0][h-1] + 1           # h번째 인덱스에 이전 보자기의 횟수에 1을 더해 저장한다
        dp[1][h] = dp[1][h-1]               # h번째 인덱스에 이전 바위의 횟수와 똑같이 저장한다
        dp[2][h] = dp[2][h-1]               # h번째 인덱스에 이전 가위의 횟수와 똑같이 저장한다
    elif HPS[h] == 'H':                     # h번째 주먹을 냈다면
        dp[0][h] = dp[0][h-1]               # h번째 인덱스에 이전 보자기의 횟수와 똑같이 저장한다
        dp[1][h] = dp[1][h-1] + 1           # h번째 인덱스에 이전 바위의 횟수에 1을 더해 저장한다
        dp[2][h] = dp[2][h-1]               # h번째 인덱스에 이전 가위의 횟수와 똑같이 저장한다
    else:                                   # h번째 가위를 냈다면
        dp[0][h] = dp[0][h-1]               # h번째 인덱스에 이전 보자기의 횟수와 똑같이 저장한다
        dp[1][h] = dp[1][h-1]               # h번째 인덱스에 이전 바위의 횟수와 똑같이 저장한다
        dp[2][h] = dp[2][h-1] + 1           # h번째 인덱스에 이전 가위의 횟수에 1을 더해 저장한다
ans = 0                                     # 정답을 저장할 변수를 생성하고
for i in range(N):                          # 가위바위보 횟수를 반복해서
    tmp1 = max(dp[0][i] + (dp[1][N-1]-dp[1][i]), dp[0][i] + (dp[2][N-1]-dp[2][i]))  # i번까지 보자기로 이긴 횟수 + 바위로 바꿨을 때 이길 횟수 / i번까지 보자기로 이긴 횟수 + 가위로 바꿨을 때 이길 횟수 중 큰 값을 tmp1에 저장한다
    tmp2 = max(dp[1][i] + (dp[0][N-1]-dp[0][i]), dp[1][i] + (dp[2][N-1]-dp[2][i]))  # i번까지 바위로 이긴 횟수 + 보자기로 바꿨을 때 이길 횟수 / i번까지 바위로 이긴 횟수 + 가위로 바꿨을 때 이길 횟수 중 큰 값을 tmp1에 저장한다
    tmp3 = max(dp[2][i] + (dp[0][N-1]-dp[0][i]), dp[2][i] + (dp[1][N-1]-dp[1][i]))  # i번까지 가위로 이긴 횟수 + 보자기로 바꿨을 때 이길 횟수 / i번까지 가위로 이긴 횟수 + 바위로 바꿨을 때 이길 횟수 중 큰 값을 tmp1에 저장한다
    ans = max(ans, tmp1, tmp2, tmp3)        # ans와 tmp1, tmp2, tmp3 중 가장 많은 승리 횟수로 ans에 저장한다
print(ans)                                  # 이길 수 있는 최대 게임 수를 출력한다