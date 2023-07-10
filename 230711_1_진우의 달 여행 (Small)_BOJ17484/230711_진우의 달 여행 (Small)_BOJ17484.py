# 진우의 달 여행 (Small)_BOJ17484

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                                                        # N 행의 길이 / M 열의 길이
dp = [[[6000]*3] + [[k]*3 for k in list(map(int, input().split()))] + [[6000]*3]]       # 출발지점의 연료를 dp 리스트에 넣어 저장한다 (앞 뒤에 최대값인 6000을 넣어 index에러를 막아준다)
for i in range(N-1):                                                                    # 남은 행을 반복해서
    fuel = list(map(int, input().split()))                                              # 다음 행의 비용을 리스트로 input 받은 후
    tmp_dp = [[6000]*3] + [[0]*3 for _ in range(M)] + [[6000]*3]                        # 해당 행까지 드는 연료량을 저장할 리스트를 생성한다
    for j in range(1, M+1):                                                             # 각 열을 반복해서
        tmp_dp[j][0] = min(dp[i][j + 1][1], dp[i][j + 1][2]) + fuel[j-1]                # 왼쪽으로 내려갈 경우 오른쪽 상단에서 수직으로 내려온값과 오른쪽으로 내려온 값 중 최소값과 현재 연료를 더해 저장
        tmp_dp[j][1] = min(dp[i][j][0], dp[i][j][2]) + fuel[j-1]                        # 수직으로 내려갈 경우 수직 상단에서 왼쪽으로 내려온값과 오른쪽으로 내려온 값 중 최소값과 현재 연료를 더해 저장
        tmp_dp[j][2] = min(dp[i][j - 1][0], dp[i][j - 1][1]) + fuel[j-1]                # 오른쪽으로 내려갈 경우 왼쪽 상단에서 왼쪽으로 내려온값과 수직으로 내려온 값 중 최소값과 현재 연료를 더해 저장
    dp.append(tmp_dp)                                                                   # 해당행의 최소비용을 저장한 리스트를 dp 리스트에 append

ans = 6000                                                                              # 최소 연료를 저장할 변수를 생성하고
for i in dp[-1]:                                                                        # 마지막 행을 반복해서
    if ans > min(i):                                                                    # ans보다 i 원소의 최소비용이 더 작다면
        ans = min(i)                                                                    # ans를 i 원소의 최소비용으로 갱신한다
print(ans)                                                                              # 최소비용의 연료값을 출력한다