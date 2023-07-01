# 투자의 귀재 배주형_BOJ19947

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

# input 받기
H, Y = map(int, input().split())                                                # H 초기 비용 / Y 투자 햇수
dp = [0] * (Y + 1)                                                              # 이자를 얻은 비용을 저장할 리스트 생성
dp[0] = H                                                                       # 초기 비용을 0번 인덱스에 저장
for y in range(1, Y+1):                                                         # 1부터 Y까지 햇수를 반복해서
    if y >= 5:                                                                  # 5 이상인 경우
        dp[y] = math.trunc(max(dp[y-1] * 1.05, dp[y-3] * 1.2, dp[y-5] * 1.35))  # 작년에서 5퍼센트 이자를 붙인 금액과 3년전에서 20퍼센트 이자를 붙인 금액과 5년전에서 35퍼센트 이자를 붙인 금액 중 큰 금액을 소수점 이하 버림하여 저장한다
    elif y >= 3:                                                                # 3 이상인 경우
        dp[y] = math.trunc(max(dp[y-1] * 1.05, dp[y-3] * 1.2))                  # 작년에서 5퍼센트 이자를 붙인 금액과 3년전에서 20퍼센트 이자를 붙인 금액 중 큰 금액을 소수점 이하 버림하여 저장한다
    else:                                                                       # 3 미만인 경우
        dp[y] = math.trunc(dp[y-1] * 1.05)                                      # 작년에서 5퍼센트 이자를 붙인 금액을 소수점 이하 버림하여 저장한다
print(dp[-1])                                                                   # Y년 후 총 자산을 출력한다