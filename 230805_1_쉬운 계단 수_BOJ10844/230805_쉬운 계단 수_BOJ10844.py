# 쉬운 계단 수_BOJ10844

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                        # 계단수 길이를 input 받고
dp = [[0] * 10 for _ in range(N+1)]                     # 계단수의 개수를 저장할 리스트를 생성한다
for i in range(1, 10):                                  # 계단수의 길이가 1인 경우에는 1부터 9까지 모두 계단 수 이므로
    dp[1][i] = 1                                        # 리스트에 계단수를 1개씩 모두 저장한다
for i in range(2, N+1):                                 # 계단수의 길이를 2부터 N까지 반복하고
    for j in range(10):                                 # 마지막 자리의 수를 0부터 9까지 반복해서
        if j == 0:                                      # 마지막 자리가 0인 경우에는
            dp[i][j] = dp[i-1][1]                       # 이전 수가 1인 경우만 가능하므로 해당 수를 저장하고
        elif j == 9:                                    # 마지막 자리가 9인 경우에는
            dp[i][j] = dp[i-1][8]                       # 이전 수가 8인 경우만 가능하므로 해당 수를 저장하고
        else:                                           # 마지막 자리가 0, 9가 아닌 경우에는
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]      # 이전 수가 j의 앞 뒤인 경우가 가능하므로 해당 수를 더해서 저장한다
print(sum(dp[N]) % 1000000000)                          # 계단수의 개수를 1000000000으로 나눈 나머지를 출력한다