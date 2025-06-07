# 별 찍기 - 17_BOJ10992

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                        # 별찍기할 숫자를 input받고
for n in range(N):                                      # 숫자를 반복해서
    if n == N-1:                                        # 마지막 줄이라면
        print('*'*(2*N-1))                              # 2*N-1의 별을 출력하고
    elif n == 0:                                        # 첫줄이라면
        print(' '*(N-1)+'*')                            # 중간에 별 하나를 출력하고
    else:                                               # 중간줄이라면
        print(' '*(N-n-1) + '*' + ' '*(2*n-1) + '*')    # 중간에 간격을 벌리며 별을 출력한다