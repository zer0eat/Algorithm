# 퇴사2_BOJ1149

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                            # 근무일을 input 받고
day = [list(map(int, input().split())) for _ in range(N)]                   # 날짜별 상담기간과 비용을 리스트로 input 받느다
dp = [0] * (N+1)                                                            # 최대 비용을 저장할 리스트를 생성하고
for i in range(N):                                                          # 날짜를 반복해서
    dp[i] = max(dp[i], dp[i-1])                                             # i와 i-1일까지 번 비용 중 더 큰 값을 i일에 저장하고
    if i+day[i][0] <= N:                                                    # i일 상담을 진행했을 때 퇴사 전에 끝난다면
        dp[i+day[i][0]] = max(dp[i+day[i][0]], dp[i]+day[i][1])             # i일 상담 진행 후 날짜에 최댓값을 저장한다
print(max(dp))                                                              # 얻을 수 있는 최대 이익을 출력한다