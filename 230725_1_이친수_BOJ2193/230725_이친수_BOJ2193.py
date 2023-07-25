# 이친수_BOJ2193

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 자리수를 input 받고
dp = [1] * N                        # 각 자리수마다 이친수의 개수를 저장할 리스트 생성
for i in range(2, N):               # 3자리수부터 N자리까지 반복해서
    dp[i] = dp[i-1] + dp[i-2]       # 해당 자리수의 이친수를 계산해 저장한다
print(dp[-1])                       # N자리 이친수의 개수를 출력한다