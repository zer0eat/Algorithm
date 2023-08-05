# 01타일_BOJ1904

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 타일의 길이를 input 받고
dp = [0] * (N+1)                            # N개의 타일로 만들 수 있는 경우의 수를 저장할 리스트를 생성한다
dp[0] = 1                                   # 길이가 0인 경우의 수를 1로 저장하고
dp[1] = 1                                   # 길이가 1인 경우의 수를 1로 저장한 후
for i in range(2, N+1):                     # 2부터 N까지 반복해서
    dp[i] = (dp[i-1] + dp[i-2]) % 15746     # 길이가 i인 경우의 수를 i-1 타일 뒤에 1을 붙인 경우와 i-2 타일 뒤에 00을 붙인 경우를 더해 저장한다
print(dp[N])                                # 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지를 출력한다