# 가장 큰 증가하는 부분 수열_BOJ11055

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # 수열의 크기
lst = list(map(int, input().split()))           # 수열을 리스트로 input 받는다
dp = [1] * N                                    # 수열의 인덱스마다 최대 수열이 되는 값을 저장할 리스트 생성
dp[0] = lst[0]                                  # 수열의 첫번째 값을 dp의 0번 리스트에 저장하고
for i in range(1, N):                           # 1부터 N-1까지 반복하고
    for j in range(i):                          # i번째 원소 이전의 원소를 반복해서
        if lst[i] > lst[j]:                     # i번째 원소가 j보다 클 때
            dp[i] = max(dp[i], dp[j]+lst[i])    # dp[i]에 현재 dp[i]와 dp[j]에서 i번째 원소를 더한 값 중 큰 값으로 갱신한다
        else:                                   # i번째 원소가 j보다 작거나 같을 때
            dp[i] = max(dp[i], lst[i])          # dp[i]에 현재 dp[i]와 i번째 원소 중 큰 값으로 갱신한다
print(max(dp))                                  # dp에서 증가하는 부분수열의 합이 가장 큰 수를 출력한다