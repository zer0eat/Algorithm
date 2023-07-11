# 퇴사_BOJ14501

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                # 퇴사까지 남은 날
consult = [list(map(int, input().split())) for _ in range(N)]   # N일 동안 잡혀있는 상담 일정을 리스트로 input 받고
dp = [0] * (N+1)                                                # 매일 최대 비용을 저장할 dp 리스트 생성

for i in range(N):                                              # 퇴사까지 남은 날을 반복해서
    for j in range(i+consult[i][0], N+1):                       # i번째 상담이 끝나는 날짜부터 퇴사일까지 반복해서
        if dp[j] < dp[i] + consult[i][1]:                       # i일까지 번 수익에 i번 상담을 한 비용의 합이 j일에 저장된 비용보다 크다면
            dp[j] = dp[i] + consult[i][1]                       # j일의 비용을 갱신한다
print(dp[-1])                                                   # 퇴사까지 모든 스케줄을 점검 후 최대 수익을 출력한다