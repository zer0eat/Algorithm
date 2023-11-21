# 악수_BOJ8394

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 회의에 참석한 사람의 수를 input받고
dp = [0]*(N+1)                          # 악수 횟수를 저장할 리스트를 생성하고
dp[1] = 1                               # 사람이 한명인 경우 악수를 안하는 1가지 경우의 수를 저장한다
dp[2] = 2                               # 사람이 두명인 경우 악수를 하거나 안하는 2가지 경우의 수를 저장한다
for i in range(3, N+1):                 # 3부터 N까지 반복해서
    dp[i] = (dp[i-1] + dp[i-2]) % 10    # i명이 할 수 있는 경우의 수를 1의 자리만 저장하고
print(dp[N])                            # N명이 악수할 수 있는 경우의 수를 출력한다