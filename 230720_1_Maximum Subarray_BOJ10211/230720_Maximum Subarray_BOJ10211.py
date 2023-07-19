# Maximum Subarray_BOJ10211

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                                    # 테스트 케이스
for t in range(T):                                  # 테스트 케이스를 반복해서
    N = int(input())                                # 수열의 길이
    lst = list(map(int, input().split()))           # 수열을 리스트로 input 받고
    dp = [0] * N                                    # 최대 부분수열을 저장할 리스트를 생성한다
    for i in range(N):                              # 부분수열 리스트를 반복해서
        dp[i] = max(lst[i] + dp[i-1], lst[i])       # 최대 부분수열 리스트에 수열의 i번째 원소와 이전 원소까지 최대 값과 i번째 원소의 합 중 더 큰 값을 저장한다
    print(max(dp))                                  # 부분 수열리스트를 마쳤다면 dp에 저장된 값 중 최대값을 출력해 최대 부분수열의 합을 출력한다