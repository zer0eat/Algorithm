# 동전1_BOJ2293

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())            # N 동전의 종류 / K 동전의 합
coin = [int(input()) for _ in range(N)]     # 동전의 종류를 input 받아 리스트로 저장한 후
dp = [0] * (K + 1)                          # 0부터 K까지 인덱스로 리스트를 생성하고
dp[0] = 1                                   # 0번째 인덱스에 1을 저장한다
for c in coin:                              # 동전의 종류를 반복하고
    for d in range(1, K+1):                 # 동전의 합을 1부터 K까지 반복해서
        if d - c >= 0:                      # 동전의 합이 동전보다 크거나 같다면
            dp[d] += dp[d-c]                # d 인덱스에 d-c 인덱스의 원소를 더해준다
print(dp[K])                                # K번째 인덱스의 동전의 합 경우의 수를 출력한다