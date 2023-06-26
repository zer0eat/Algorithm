# 2×n 타일링 2_BOJ11727

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
n = int(input())                                # 가로의 칸수를 input 받고
if n % 2 == 0:                                  # 가로가 짝수인 경우
    dp = [3]                                    # dp에 2칸일 때 경우의수 3을 넣은 리스트를 생성하고
    for i in range(1, n//2):                    # 짝수칸만 반복해서
        dp.append((dp[i-1] * 4 - 1) % 10007)    # 이전 짝수 칸의 4배보다 1 작은 수가 다음 짝수 칸의 경우의 수이므로 10007로 나눈 나머지를 append
else:                                           # 가로가 홀수인 경우
    dp = [1]                                    # dp에 1칸일 때 경우의수 1을 넣은 리스트를 생성하고
    for i in range(1, n//2+1):                  # 홀수칸만 반복해서
        dp.append((dp[i-1] * 4 + 1) % 10007)    # 이전 홀수 칸의 4배보다 1 큰 수가 다음 홀수 칸의 경우의 수이므로 10007로 나눈 나머지를 append
print(dp[-1])                                   # n칸의 경우의 수를 출력한다