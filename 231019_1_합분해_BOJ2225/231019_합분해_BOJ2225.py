# 합분해_BOJ2225

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())                            # N 구하려는 합 / K N을 만들기 위해 더해야하는 정수의 개수
dp = [[0]*(N+1) for _ in range(K+1)]                        # 0부터 N까지 열을 갖고 0부터 K까지 행을 갖는 행렬을 생성한다
dp[0][0] = 1                                                # dp의 0,0 위치에 1을 저장하고
for i in range(N+1):                                        # 열을 반복해고
    for j in range(1, K+1):                                 # 행을 반복해서
        dp[j][i] = (dp[j-1][i] + dp[j][i-1]) % 1000000000   # 0부터 i까지 정수 j개를 더해 i가 되는 경우의 수를 1000000000으로 나눈 나머지를 저장한다
print(dp[K][N])                                             # 0부터 N까지 정수 K개를 더해 N이 되는 경우의 수를 출력한다