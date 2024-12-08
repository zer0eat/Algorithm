# Loteria Falha_BOJ30664

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                            # break가 나올때까지 반복해서
    N = int(input())                # 숫자를 input 받고
    if N == 0:                      # 0이 나오면
        break                       # while문을 종료하고
    else:                           # 0이 아니면
        if N % 42:                  # 42의 배수가 아니라면
            print('TENTE NOVAMENTE')# 다시시도를 출력하고
        else:                       # 42의 배수라면
            print('PREMIADO')       # 수상을 출력한다