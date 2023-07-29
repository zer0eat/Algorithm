# 1, 2, 3 더하기 4_BOJ15989

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                        # 테스트 케이스
for t in range(T):                      # 테스트 케이스를 반복해서
    N = int(input())                    # 정수 N을 input 받고
    dp = [1] * (N+1)                    # 0부터 N까지 원소를 갖는 리스트를 생성한다
    for i in range(2, 4):               # 2, 3의 경우를 반복해서
        for j in range(i, N+1):         # i부터 N까지 반복할 때
            dp[j] = dp[j] + dp[j-i]     # j번째 원소는 j번째 원소와 j-1번째 원소의 합으로 경우의 수를 구한다
    print(dp[-1])                       # N을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다