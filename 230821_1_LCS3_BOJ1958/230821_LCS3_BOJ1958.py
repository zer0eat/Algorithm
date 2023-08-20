# LCS3_BOJ1958

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
word1 = input().strip()                                                             # 첫번째 문자열을 input 받고
word2 = input().strip()                                                             # 두번째 문자열을 input 받고
word3 = input().strip()                                                             # 세번째 문자열을 input 받은 후
w1 = len(word1)+1                                                                   # 첫번째 문자열의 길이에 1을 더한 변수를 생성하고
w2 = len(word2)+1                                                                   # 두번째 문자열의 길이에 1을 더한 변수를 생성하고
w3 = len(word3)+1                                                                   # 세번째 문자열의 길이에 1을 더한 변수를 생성한다
dp = [[[0]*w3 for _ in range(w2)] for _ in range(w1)]                               # LCS를 저장할 3차원 배열을 생성한다
for i in range(1, w1):                                                              # 1부터 첫번째 문자열의 길이만큼 반복하고
    for j in range(1, w2):                                                          # 1부터 두번째 문자열의 길이만큼 반복해고
        for k in range(1, w3):                                                      # 1부터 두번째 문자열의 길이만큼 반복해서
            if word1[i-1] == word2[j-1] == word3[k-1]:                              # i번째 첫번째 문자와 j번째 두번째 문자와 k번째 세번째 문자가 같다면
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1                                 # dp의 (i, j, k)의 원소에 이전까지 개수에서 1 더한 값을 저장한다
            else:                                                                   # 세 문자중 한개라도 다르다면
                dp[i][j][k] = max(dp[i][j][k-1], dp[i][j-1][k], dp[i-1][j][k])      # (i-1, j, k) / (i, j-1, k) / (i, j, k-1)의 원소 중 가장 큰 값을 저장한다
print(dp[w1-1][w2-1][w3-1])                                                         # 부분 수열 중 가장 긴 문자열의 길이를 출력한다