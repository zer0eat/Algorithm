# 타일 채우기_BOJ2133

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 벽의 가로의 길이를 input 받고
if N % 2 == 1:                      # 벽의 가로 길이가 홀수인 경우
    print(0)                        # 타일로 채울 수 없으므로 경우의 수 0을 출력한다
else:                               # 벽의 가로 길이가 짝수인 경우
    dp = [0] * (N+1)                # 경우의 수를 저장할 리스트를 생성하고
    dp[0] = 1                       # 0일 때 1로 저장한다
    for i in range(2, N+1, 2):      # 2부터 N까지 짝수 번호만 반복해서
        dp[i] = dp[i-2] * 3         # 가로 길이가 i일 때 이전 타일에서 2칸을 채우는 방법이 3가지 있으므로 3배를 곱해서 저장한다
        for j in range(0, i-2, 2):  # 0부터 i-3까지 짝수 길이만 반복해서
            dp[i] += dp[j] * 2      # i의 경우의 수에 j칸 이후 나머지 길이를 길게 붙이는 경우의 수 2가지가 있으므로 2배를 곱해서 더한다
    print(dp[N])                    # 길이가 N개일 때 경우의 수를 출력한다