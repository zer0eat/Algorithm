# 별 찍기 - 16_BOJ10991

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 줄의 수를 input받고
for M in range(1, N+1):                     # 줄의 개수를 반복해서
    for n in range(M):                      # M개만큼 반복해서
        if n == 0:                          # 첫번째라면
            print(' '*(N-M) + '*', end='')  # N-M만큼 띄어쓰고 별을 출력하고
        else:                               # 첫번째가 아니라면
            print(' ' + '*', end='')        # 한칸 띄고 별을 출력한다
    else:                                   # 한줄이 끝났다면
        print()                             # 줄을 바꿔준다