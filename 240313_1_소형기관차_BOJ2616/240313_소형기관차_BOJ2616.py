# 소형기관차_BOJ2616

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 기관차의 객차의 수를 input 받고
lst = [0] + list(map(int, input().split())) # 객차별 사람의 수를 리스트로 input 받는다
T = int(input())                            # 소형기관차가 끌 수 있는 객차의 개수를 input 받고
dp = [[0]*(N+1) for _ in range(4)]          # dp 리스트를 생성한다
for i in range(1, 4):                       # 객차의 수를 반복해서
    for j in range(T*i, N+1):               # 소형기관차를 끌 객차를 반복해서
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-T] + sum(lst[j-T+1:j+1]))  # 이전까지 최대 운송수와 현재 객차를 포함한 최대 운송수 중 더 큰값으로 저장한다
print(dp[-1][-1])                           # 소형 기관차 3대를 이용하여 최대로 운송할 수 있는 손님 수를 출력한다