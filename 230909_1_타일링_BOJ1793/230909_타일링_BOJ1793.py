# 타일링_BOJ1793

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
dp = [0] * 251                          # 0부터 250 경우의 수를 셀 리스트를 생성하고
dp[0] = 1                               # 가로의 길이가 0일 때 경우의 수 1을 저장하고
dp[1] = 1                               # 가로의 길이가 1일 때 경우의 수 1을 저장하고
for i in range(2, 251):                 # 2부터 250까지 반복해서
    dp[i] = dp[i-2]*2 + dp[i-1]         # 해당 길이일 때 경우의 수를 리스트에 저장한다
while 1:                                # break가 나올 때까지 반복해서
    try:                                # input 받을 숫자가 있으면
        print(dp[int(input())])         # 가로의 길이가 input 받은 숫자일 때 경우의 수를 출력하고
    except:                             # input 받을 숫자가 없으면
        break                           # while문을 break 한다