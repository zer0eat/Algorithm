# 1, 2, 3 더하기 5_BOJ15990

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
dp = [[0, 0, 0] for _ in range(100001)]                     # 0부터 100000까지 원소를 갖는 리스트를 생성한다
dp[1] = [1, 0, 0]                                           # 1을 1, 2, 3의 합으로 나타내는 방법의 수 1번 인덱스에 저장한다
dp[2] = [0, 1, 0]                                           # 2를 1, 2, 3의 합으로 나타내는 방법의 수 2번 인덱스에 저장한다
dp[3] = [1, 1, 1]                                           # 3을 1, 2, 3의 합으로 나타내는 방법의 수 3번 인덱스에 저장한다
for j in range(4, 100001):                                  # 4부터 100000까지 반복해서
    dp[j][0] = (dp[j-1][1] + dp[j-1][2] % 1000000009)       # j를 1을 마지막으로 더했을 때 나타내는 방법의 수 j번의 0번 인덱스에 저장한다
    dp[j][1] = (dp[j-2][0] + dp[j-2][2] % 1000000009)       # j를 2를 마지막으로 더했을 때 나타내는 방법의 수 j번의 1번 인덱스에 저장한다
    dp[j][2] = (dp[j-3][0] + dp[j-3][1] % 1000000009)       # j를 3을 마지막으로 더했을 때 나타내는 방법의 수 j번의 2번 인덱스에 저장한다
T = int(input())                                            # 테스트 케이스 input 받고
for t in range(T):                                          # 테스트 케이스를 반복해서
    N = int(input())                                        # 정수 N을 input 받고
    print(sum(dp[N]) % 1000000009)                          # N을 1, 2, 3의 합으로 나타내는 방법의 수를 1000000009로 나눈 나머지를 출력한다