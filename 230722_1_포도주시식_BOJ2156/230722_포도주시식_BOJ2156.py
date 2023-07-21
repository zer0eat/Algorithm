# 포도주시식_BOJ2156

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                                    # 포도주 잔의 개수를 input 받고
wine = []                                                                           # 포도주의 양을 저장할 리스트를 생성한다
dp = [0] * N                                                                        # 최대 포도주양을 저장할 리스트를 생성하고
for i in range(N):                                                                  # 포도주 잔의 개수를 반복한다
    wine.append(int(input()))                                                       # 포도주의 양을 wine에 append 한 후
    if i == 0:                                                                      # 첫번째 잔인 경우
        dp[i] = wine[i]                                                             # 첫번째 잔을 다 마신 경우가 최댓값이므로 dp에 첫번째 잔의 양을 저장한다
    elif i == 1:                                                                    # 두번째 잔인 경우
        dp[i] = wine[i] + dp[i-1]                                                   # 첫번째와 두번째 잔을 다 마신 경우가 최댓값이므로 dp에 첫번째 잔과 두번째 잔의 양을 저장한다
    else:                                                                           # 세번째 이상인 경우
        dp[i] = max(dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i], dp[i-1])      # 2번째 전잔과 현재 잔 / 세번째 전잔과 이전 잔 현재 잔 / 현재잔을 마시지 않을 경우 중 가장 많은 양의 포도주를 dp에 저장한다
print(dp[-1])                                                                       # 최대로 마실 수 있는 포도주의 양을 출력한다