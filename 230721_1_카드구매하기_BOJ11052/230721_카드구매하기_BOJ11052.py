# 카드구매하기_BOJ11052

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # 카드의 개수
lst = [0] + list(map(int, input().split()))     # 카드의 금액을 리스트 형태로 input 받고
dp = [0] * (N+1)                                # 금액별 최대 비용을 저장할 리스트를 생성한다

for i in range(N+1):                            # N까지 반복해서
    for j in range(1, i+1):                     # 1부터 i까지 반복한 후
        dp[i] = max(dp[i], dp[i-j] + lst[j])    # i개의 카드를 구매할 때 현재 저장된 금액과 i-j / j 개의 카드 팩을 나눠 살때 비용 중 최대 금액을 저장한다
print(dp[-1])                                   # 반복을 모두 마쳤다면 N개의 카드를 구매할 때 최대 금액을 출력한다