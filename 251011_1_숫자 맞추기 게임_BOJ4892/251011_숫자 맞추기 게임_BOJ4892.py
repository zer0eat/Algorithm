# 숫자 맞추기 게임_BOJ4892

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
tmp = 1                                 # 순서를 저장할 변수를 생성하고
while 1:                                # 0이 나올때까지 반복해서
    N = int(input())                    # 숫자를 input받고
    if N == 0:                          # 숫자가 0이라면
        break                           # while문을 종료하고
    if N % 2:                           # 숫자가 홀수라면
        print(f'{tmp}. odd {N//2}')     # 순서와 몫을 출력하고
    else:                               # 숫자가 짝수라면
        print(f'{tmp}. even {N//2}')    # 순서와 몫을 출력한다
    tmp += 1                            # 순서를 1 추가한다