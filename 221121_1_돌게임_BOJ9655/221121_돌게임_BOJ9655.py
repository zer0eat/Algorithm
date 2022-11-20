# 돌게임_BOJ9655

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())   # 돌멩이의 수

cnt = 0                         # 차례를 셀 변수를 생성하고
while N > 0:                    # N이 0이 될때까지 반복해서
    if N >= 3:                  # N이 3보다 같거나 클때는
        N -= 3                  # N에서 3을 빼고
        cnt += 1                # cnt를 1 더한다
    else:                       # N이 3보다 작다면
        N -= 1                  # N에서 1을 빼고
        cnt += 1                # cnt를 1 더한다

if cnt % 2:                     # cnt가 홀수이면
    print('SK')                 # SK를 출력하고
else:                           # cnt가 짝수이면
    print('CY')                 # CY를 출력한다