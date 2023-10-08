# 한글 LCS_BOJ15482

# input.txt 열기
import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')    # 한글을 받기 위해 utf-8로 인코딩해서 open
input = sys.stdin.readline

# input 받기
# -*- coding: utf-8 -*-                                 # 인코딩 명시를 해준 후
A = input().strip()                                     # 첫번째 단어를 input 받고
B = input().strip()                                     # 두번째 단어를 input 받는다
N = len(A)                                              # 첫번째 단어의 길이를 A에 저장하고
M = len(B)                                              # 두번째 단어의 길이를 b에 저장한다
dp = [[0]*(M+1) for _ in range(N+1)]                    # LCS를 저장하기 위한 dp를 생성하고
for i in range(1, N+1):                                 # A의 글자를 반복하고
    for j in range(1, M+1):                             # B의 글자를 반복해서
        if A[i - 1] == B[j - 1]:                        # A[i - 1]와 B[j - 1]의 글자가 같다면
            dp[i][j] = dp[i-1][j-1] + 1                 # A[i-1]와 B[j-1]의 LCS에서 1을 추가한 값을 dp[i][j]에 저장하고
        else:                                           # 같지 않다면
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])      # A[i]와 B[j-1]의 LCS와 A[i-1]와 B[j]의 LCS 중 큰 값을 dp[i][j]에 저장한다
print(dp[N][M])                                         # A와 B의 LCS를 출력한다