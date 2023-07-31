# 돌게임3_BOJ9657

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 돌의 개수를 input 받고
dp = [0] * 5                    # 승리자를 저장할 리스트를 생성하고
dp[1] = 'SK'                    # 돌이 한개일 때 상근이가 이기므로 SK로 저장
dp[2] = 'CY'                    # 돌이 두개일 때 창영이가 이기므로 CY로 저장
dp[3] = 'SK'                    # 돌이 세개일 때 상근이가 이기므로 SK로 저장
dp[4] = 'SK'                    # 돌이 네개일 때 상근이가 이기므로 SK로 저장
for i in range(5, N+1):         # 5부터 N개까지 돌일 때 반복해서
    for j in (1, 3, 4):         # 가져갈 수 있는 돌의 개수를 반복한다
        if dp[i-j] == 'CY':     # i개의 돌에서 j개를 뺏을 때 창영이가 이기는 경우
            dp.append('SK')     # i개 돌의 승리자는 상근이가 되므로 SK를 append하고
            break               # for문을 break한다
    else:                       # 돌의 개수를 반복했을 때 모두 SK가 이기는 경우
        dp.append('CY')         # i개 돌의 승리자는 창영이가 되므로 CY를 append한다
print(dp[N])                    # N개의 돌의 승리자를 출력한다