# 카드 구매하기2_BOJ16194

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 구매하려는 카드의 개수를 input 받고
card = [0] + list(map(int, input().split()))        # 1개부터 N개까지 카드팩의 가격을 리스트로 input 받고 0번 원소에 0을 추가한다
dp = [10000001] * (N+1)                             # 카드 개수 별 구매 금액을 저장할 리스트를 생성하고
dp[0] = 0                                           # 0개를 구매할 때 금액을 0으로 저장한다
for i in range(1, N+1):                             # 구매하려는 카드의 개수를 1부터 N까지 반복하고
    for j in range(1, N+1):                         # 카드 팩을 반복해서
        if i < j:                                   # 카드 수보다 카드 팩의 수가 크다면
            break                                   # for문을 break
        dp[i] = min(dp[i], card[j] + dp[i-j])       # i개 카드 구매 금액을 현재 저장된 금액과 j개와 나머지 최소금액 중  더 적은 금액으로 저장한다
print(dp[N])                                        # 카드 N개를 갖기 위해 지불해야 하는 금액의 최솟값을 출력한다