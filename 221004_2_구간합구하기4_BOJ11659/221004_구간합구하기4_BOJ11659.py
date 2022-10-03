# 구간합구하기4_BOJ11659

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, T = map(int, sys.stdin.readline().split())               # N 수열 / T 테스트 케이스
arr = list(map(int, sys.stdin.readline().split()))          # 수열을 리스트에 input

dp = [0] * (N + 1)                                          # dp 현재인덱스까지의 합을 저장하기 위한 리스트
for n in range(N):                                          # arr의 전체를 반복할 때
    dp[n + 1] = dp[n] + arr[n]                              # 현재 인덱스까지의 합을 저장한다

for t in range(T):                                          # 테스트 케이스를 반복할 때
    i, j = map(int, sys.stdin.readline().split())           # 시작점과 끝점을 input 받고
    print(dp[j] - dp[i - 1])                                # 두점까지의 합의 차를 출력한다