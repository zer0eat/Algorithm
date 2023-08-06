# 이동하기_BOJ11048

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                                # N 행의 길이 / M 열의 길이를 input 받고
miro = [list(map(int, input().split())) for _ in range(N)]      # 미로에 놓인 사탕의 정보를 리스트로 input 받는다
dp = [[0] * M for _ in range(N)]                                # 각 위치별 가장 많은 사탕을 가져갈 정보를 저장할 리스트를 생성한다
for i in range(M):                                              # 첫번째 행의 원소를 반복해서
    dp[0][i] = dp[0][i-1] + miro[0][i]                          # dp의 [0][i]에 miro의 [0][i]에 놓인 사탕과 이전 칸에 놓인 사탕의 합을 저장한다
for j in range(N):                                              # 첫번째 열의 원소를 반복해서
    dp[j][0] = dp[j-1][0] + miro[j][0]                          # dp의 [j][0]에 miro의 [j][0]에 놓인 사탕과 이전 칸에 놓인 사탕의 합을 저장한다
for i in range(1, N):                                           # 두번째 행부터 끝까지 반복하고
    for j in range(1, M):                                       # 두번째 열부터 끝까지 반복해서
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + miro[i][j]       # dp의 [i][j]에 miro의[i][j]에 놓인 사탕과 왼쪽 / 위쪽 / 왼쪽상단 칸에 놓인 사탕 중 가장 큰 값과 합을 저장한다
print(dp[N-1][M-1])                                             # (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수를 출력한다