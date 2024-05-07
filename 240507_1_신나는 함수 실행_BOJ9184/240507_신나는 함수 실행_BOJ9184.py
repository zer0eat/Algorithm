# 신나는 함수 실행_BOJ9184

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:                                                  # a, b, c 중 하나라도 0 이하라면
        return 1                                                                    # 1을 리턴한다
    if a > 20 or b > 20 or c > 20:                                                  # a, b, c 모두가 20초과라면
        return w(20, 20, 20)                                                        # w(20, 20, 20)을 리턴한다
    if dp[a][b][c]:                                                                 # dp[a][b][c]에 값이 저장되어 있다면
        return dp[a][b][c]                                                          # dp[a][b][c]를 리턴한다
    if a < b < c:                                                                   # a < b < c 라면
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)                  # dp[a][b][c]에 w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)의 값을 저장하고
        return dp[a][b][c]                                                          # dp[a][b][c]를 리턴한다
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1) # dp[a][b][c]에 w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)의 값을 저장하고
    return dp[a][b][c]                                                              # dp[a][b][c]를 리턴한다

dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]                             # 미리 계산할 값을 저장할 dp를 생성하고
while 1:                                                                            # break가 나올 때까지 반복해서
    a, b, c = map(int, input().split())                                             # a, b, c를 input 받고
    if [a, b, c] == [-1, -1, -1]:                                                   # a, b, c가 모두 -1이라면
        break                                                                       # while문을 break한다
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')                                       # 입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다