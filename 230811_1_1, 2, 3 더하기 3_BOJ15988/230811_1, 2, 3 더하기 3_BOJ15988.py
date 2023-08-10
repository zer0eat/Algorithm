# 1, 2, 3 더하기 3_BOJ15988

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
dp = [0] * 1000001                                          # 0부터 1000000까지 원소를 갖는 리스트를 생성
dp[0] = 1                                                   # 인덱스가 0일 때 1로 저장 하고
for i in range(1, 1000001):                                 # 1부터 1000000까지 반복해서
    dp[i] += ((dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009)   # i의 경우의 수를 i보다 1작은 수에 1을 붙인 경우와 i보다 2작은수에 2를 붙인 경우와 i보다 3작은수에 3을 붙인 경우의 합을 1000000009로 나눈 나머지로 저장한다
T = int(input())                                            # 테스트 케이스를 input 받고
for t in range(T):                                          # 테스트 케이스를 반복해서
    N = int(input())                                        # N을 input 받은 후
    print(dp[N])                                            # N을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다