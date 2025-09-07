# SUAPC 의자 준비하기_BOJ34183

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M, A, B = map(int, input().split())  # 참석하는 팀과 의자의 수 비용을 input받고
ans = (N*3) - M                         # 필요한 의자의 수를 계산해서
if ans > 0:                             # 의자가 필요하면
    print(ans * A + B)                  # 배송비를 출력하고
else:                                   # 의자가 필요 없으면
    print(0)                            # 0원을 출력한다