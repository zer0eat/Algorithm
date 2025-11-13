# 그래서 님 푼 문제 수가?_BOJ29720

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M, K = map(int, input().split())         # N, M, K를 input받고
ans1 = N - (M*K)                            # 푼 문제의 최소값을 구하고
ans2 = ans1 + M - 1                         # 푼 문제의 최대값을 구한다
if ans1 < 0:                                # 최소값이 음수일 경우 
    ans1 = 0                                # 0으로 바꾸고
elif ans2 < 0:                              # 최대값이 음수일 경우               
    ans2 = 0                                # 0으로 바꾼다
print(ans1, ans2)                           # 최소값과 최대값을 출력한다