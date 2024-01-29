# 구간 합 구하기 5_BOJ11660

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                                            # N 표의 크기 / M 연산 횟수를 input받고
lst = [list(map(int, input().split())) for _ in range(N)]                   # 표를 input 받아 저장한다
dp = [[0]*(N+1) for _ in range(N+1)]                                        # 표의 누적합을 저장할 리스트를 생성하고
for i in range(1, N+1):                                                     # 행을 1부터 N까지 반복하고
    for j in range(1, N+1):                                                 # 열을 1부터 N까지 반복해서
        dp[i][j] = lst[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]   # dp의 i,j에 lst i-1, j-1까지의 누적합을 저장한다
for m in range(M):                                                          # 연산의 횟수를 반복해서
    x1, y1, x2, y2 = map(int, input().split())                              # 연산을 할 부분을 input 받고
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])        # x1,y1부터 x2,y2까지의 합을 출력한다