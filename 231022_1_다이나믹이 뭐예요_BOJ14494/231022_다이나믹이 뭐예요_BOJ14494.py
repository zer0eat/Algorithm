# 다이나믹이 뭐예요_BOJ14494

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                                        # N 행의 정보 / M 열의 정보를 input 받고
dp = [[0]*(M+1) for _ in range(N+1)]                                    # 행이 N+1 열이 M+1 개의 dp를 생성한다
dp[0][0] = 1                                                            # 0,0 위치에 1을 저장하고
for i in range(1, N+1):                                                 # 행을 1부터 N까지
    for j in range(1, M+1):                                             # 열을 1부터 M까지 반복해서
        dp[i][j] = (dp[i][j-1] + dp[i-1][j] + dp[i-1][j-1])%1000000007  # i,j의 원소를 1000000007로 나눈 수로 저장한다
print(dp[N][M])                                                         # N, M의 원소를 출력한다