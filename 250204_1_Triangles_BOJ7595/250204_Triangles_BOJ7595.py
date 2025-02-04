# Triangles_BOJ7595

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                    # break가 나올때까지 반복해서
    N = int(input())        # 숫자를 input 받고
    if N == 0:              # 숫자가 0이라면
        break               # while문을 break한다
    for n in range(1,N+1):  # 1부터 N까지 반복해서
        print('*'*n)        # *의 수를 출력한다