# 점수따먹기_BOJ1749

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                                            # N 행의 길이 / M 열의 길이를 input 받고
lst = [list(map(int, input().split())) for _ in range(N)]                   # 행렬의 원소를 리스트로 input 받는다
dp = [[0]*(M+1) for _ in range(N+1)]                                        # 누적합을 저장할 리스트를 생성하고
for i in range(1, N+1):                                                     # 행을 반복하고
    for j in range(1, M+1):                                                 # 열을 반복해서
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + lst[i-1][j-1]   # i,j까지의 누적합을 저장한다
ans = -1e9                                                                  # 정답을 저장할 변수를 생성하고
for i in range(1, N+1):                                                     # 행을 반복하고
    for j in range(1, M+1):                                                 # 열을 반복해서
        for r in range(i):                                                  # 부분행렬로 만들 행을 반복하고
            for c in range(j):                                              # 부분행렬로 만들 열을 반복해서
                tmp = dp[i][j] - dp[r][j] - dp[i][c] + dp[r][c]             # 부분행렬의 합을 tmp에 저장하고
                ans = max(ans, tmp)                                         # ans와 tmp 중 더 큰 값을 저장한다
print(ans)                                                                  # 부분행렬의 최대의 합을 출력한다