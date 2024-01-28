# 연속합_BOJ1912

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 수열의 길이를 input 받고
lst = list(map(int, input().split()))   # 수열을 리스트로 input 받는다
dp = [0]*N                              # 누적합을 저장할 리스트를 생성하고
for i in range(N):                      # 수열의 길이를 반복해서
    tmp = dp[i-1] + lst[i]              # 이전까지 최대합과 현재 수열의 합을 tmp에 저장하고
    if tmp < lst[i]:                    # tmp보다 현재 원소가 크다면
        dp[i] = lst[i]                  # i번째 인덱스에 현재 원소를 저장하고
    else:                               # tmp가 현재 원소보다 크다면
        dp[i] = tmp                     # i번째 인덱스에 tmp를 저장한다
print(max(dp))                          # 가장 큰 누적합을 출력한다