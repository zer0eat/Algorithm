# 직사각형과 쿼리_BOJ14846

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                                    # 행렬의 크기를 input 받고
lst = [list(map(int, input().split())) for _ in range(N)]                           # 행렬을 input 받는다
dp = [[[0]*10 for _ in range(N+1)] for _ in range(N+1)]                             # 행렬의 누적합을 저장할 리스트를 생성하고
for i in range(1, N+1):                                                             # 행을 반복하고
    for j in range(1, N+1):                                                         # 열을 반복하고
        for k in range(10):                                                         # 나올 수 있는 정수를 반복해서
            if lst[i-1][j-1] == k+1:                                                # i-1,j-1에 나온 정수가 k-1라면
                dp[i][j][k] += 1                                                    # k인덱스에 1을 추가하고
            dp[i][j][k] += dp[i-1][j][k] + dp[i][j-1][k] - dp[i-1][j-1][k]          # k인덱스에 여태까지 누적합을 저장한다
M = int(input())                                                                    # 쿼리의 수를 input 받고
for m in range(M):                                                                  # 쿼리의 수를 반복해서
    x1, y1, x2, y2 = map(int, input().split())                                      # 정수의 개수를 셀 직사각형의 시작점과 끝점을 input 받고
    ans = 0                                                                         # 서로 다른 정수의 개수를 저장할 변수를 생성하고
    for k in range(10):                                                             # 10개의 정수를 반복해서
        if dp[x2][y2][k] - dp[x2][y1-1][k] - dp[x1-1][y2][k] + dp[x1-1][y1-1][k]:   # 영역 안에 해당 정수가 있다면
            ans += 1                                                                # ans에 1을 추가한다
    print(ans)                                                                      # 서로 다른 정수의 개수를 출력한다