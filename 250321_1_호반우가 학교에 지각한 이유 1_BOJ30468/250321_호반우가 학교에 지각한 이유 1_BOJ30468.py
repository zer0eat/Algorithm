# 호반우가 학교에 지각한 이유 1_BOJ30468

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
STR, DEX, INT, LUK, N = map(int, input().split())   # 능력치를 input 받고
V = STR + DEX + INT + LUK                           # 능력치의 합을 구해서
if V >= N*4:                                        # 평균 능력치가 N보다 같거나 크다면
    print(0)                                        # 0을 출력하고
else:                                               # 평균 능력치가 N보다 작다면
    print(N*4-V)                                    # 필요한 능력치를 출력한다