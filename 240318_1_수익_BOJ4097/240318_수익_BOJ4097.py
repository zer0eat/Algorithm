# 수익_BOJ4097

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                                    # break가 나올때까지 반복해서
    N = int(input())                        # 창업 후 일자를 input 받고
    if N == 0:                              # 창업 후 지난 날이 0이라면
        break                               # break한다
    lst = [int(input()) for i in range(N)]  # N일 간 수익을 리스트에 저장하고
    dp = [-10000]*N                         # 최대 수익 구간을 구할 dp를 생성한다
    dp[0] = lst[0]                          # 첫날 수익을 저장하고
    for n in range(1, N):                   # 둘째날부터 마지막까지 반복해서
        dp[n] = max(dp[n-1]+lst[n], lst[n]) # 연속적인 날의 수익과 당일 수익 중 큰 값으로 저장한다
    print(max(dp))                          # 테스트 케이스에 대해서 가장 많은 수익을 올린 구간의 수익을 출력한다