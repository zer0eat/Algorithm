# 동전2_BOJ2294

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, K = map(int, input().split())            # N 동전의 종류 / K 동전의 합
coin = [int(input()) for _ in range(N)]     # 동전의 종류를 input 받아 리스트로 저장한 후
dp = [10001] * (K+1)                        # 금액별 최소 동전의 개수를 저장하기 위한 리스트 생성
dp[0] = 0                                   # 0원에서는 0개의 동전이 필요하기 때문에 0으로 저장
for c in coin:                              # 코인의 종류를 반복하고
    for i in range(c, K+1):                 # 코인 이상의 금액부터 K까지 반복해서
        dp[i] = min(dp[i], dp[i-c] + 1)     # i원의 원소에 현재 저장된 개수와 c코인을 추가했을 때 개수 중 더 작은 것을 저장한다
if dp[K] == 10001:                          # K원을 내기 위한 동전의 수가 10001이라면
    print(-1)                               # 낼 방법이 없으므로 -1을 출력하고
else:                                       # 10001이 아니라면
    print(dp[K])                            # 동전의 수를 출력한다