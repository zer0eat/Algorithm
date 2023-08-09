# 사자원_BOJ1309

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                        # 우리의 크기를 input받고
dp = [[1, 0] for _ in range(N+1)]                       # 경우의 수를 저장할 리스트를 생성한다
for i in range(1, N+1):                                 # 우리의 크기를 1부터 N까지 반복해서
    dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % 9901         # 마지막 줄에 우리에 사자이 비어있는 경우는 이전 줄에서 비어있거나 한마리만 있는 경우의 수의 합으로 저장하고
    dp[i][1] = (dp[i-1][0] * 2 + dp[i-1][1]) % 9901     # 마지막 줄에 우리에 사자이 한마리가 있는 경우는 이전 줄에서 비어있는 경우의 두배와 한마리만 있는 경우의 수의 합으로 저장한다
print(sum(dp[N]) % 9901)                                # 크기가 N인 우리에 사자를 배치하는 방법을 9901로 나눈 나머지로 출력한다