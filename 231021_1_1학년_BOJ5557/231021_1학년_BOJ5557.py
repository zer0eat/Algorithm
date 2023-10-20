# 1학년_BOJ5557

# input 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # 주어진 숫자의 개수를 input 받고
num = list(map(int, input().split()))           # 주어진 숫자의 목록을 list로 input 받는다
dp = [[0]*21 for _ in range(N-1)]               # N-1개의 연산시 결과를 저장할 dp를 생성하고
dp[0][num[0]] = 1                               # 첫번째 숫자를 dp에 저장한다
for i in range(1, N-1):                         # 2번째 숫자부터 N-1번째 숫자까지 반복해서
    for j in range(21):                         # 숫자의 연산결과를 0부터 20까지 반복한 후
        if dp[i-1][j]:                          # 이전 연산까지 j라는 결과가 나왔다면
            if 0<=j+num[i]<21:                  # j에서 i번째 더한 수가 0부터 20사이의 수라면
                dp[i][j+num[i]] += dp[i-1][j]   # dp[i][j+num[i]]에 이전 연산의 경우의 수를 더해주고
            if 0<=j-num[i]<21:                  # j에서 i번째 뺀 수가 0부터 20사이의 수라면
                dp[i][j-num[i]] += dp[i-1][j]   # dp[i][j-num[i]]에 이전 연산의 경우의 수를 더해준다
print(dp[-1][num[-1]])                          # 올바른 등식의 개수를 출력한다