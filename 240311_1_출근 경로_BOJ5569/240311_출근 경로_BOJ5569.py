# 출근 경로_BOJ5569

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
W, H = map(int, input().split())                            # W 행의 길이 / H 열의 길이를 input 받고
mod = 100000                                                # 나눌 수를 변수로 생성하고
dp = [[[0]*4 for i in range(H)] for j in range(W)]          # 경우의 수를 저장할 리스트를 생성한다
for i in range(1, W):                                       # 행을 반복해서
    dp[i][0][0] = 1                                         # 북쪽으로 이동하면서 동쪽으로 회전할 수 있는 경우를 1로 저장하고
for j in range(1, H):                                       # 열을 반복해서
    dp[0][j][2] = 1                                         # 동쪽으로 이동하면서 북쪽으로 회전할 수 있는 경우를 1로 저장한다
for i in range(1, W):                                       # 행을 반복하고
    for j in range(1, H):                                   # 열을 반복해서
        dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % mod # 북쪽으로 이동하면서 동쪽으로 회전할 수 있는 경우를 저장한다
        dp[i][j][1] = dp[i-1][j][2]                         # 북쪽으로 이동하면서 동쪽으로 회전할 수 없는 경우를 저장한다
        dp[i][j][2] = (dp[i][j-1][2] + dp[i][j-1][3]) % mod # 동쪽으로 이동하면서 북쪽으로 회전할 수 있는 경우를 저장한다
        dp[i][j][3] = dp[i][j-1][0]                         # 동쪽으로 이동하면서 북쪽으로 회전할 수 없는 경우를 저장한다
print(sum(dp[W-1][H-1]) % 100000)                           # 도착지에 도착할 수 있는 경우의 수를 출력한다