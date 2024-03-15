# 팰린드롬 만들기_BOJ1695

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                    # 수열의 길이를 input 받고
lst = list(map(int, input().split()))               # 수열을 리스트로 input 받는다
dp = [[0]*(N+1) for _ in range(N+1)]                # dp를 저장할 리스트를 생성한다
for i in range(1, N+1):                             # 행을 반복하고
    for j in range(1, N+1):                         # 열을 반복해서
        if lst[j-1] == lst[-i]:                     # -i번째 원소가 j-1번째 원소와 같다면
            dp[i][j] = dp[i-1][j-1] + 1             # 이전까지 비교에서 같은 수를 1 추가하고
        else:                                       # 다르다면
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])  # [i][j-1], dp[i-1][j] 중 더 큰 값으로 저장한다
print(N-dp[-1][-1])                                 # 끼워 넣을 수들의 최소 개수를 출력한다