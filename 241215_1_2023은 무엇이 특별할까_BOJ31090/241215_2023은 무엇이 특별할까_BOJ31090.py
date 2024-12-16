# 2023은 무엇이 특별할까_BOJ31090

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())        # 테스트 케이스를 input 받고
for t in range(T):      # 테스트 케이스를 반복해서
    N = int(input())    # 숫자를 input 받고
    tmp = N%100         # 숫자의 십의자리까지만 저장해서
    if (N+1) % tmp:     # N+1이 십의자리 숫자로 나눠 떨어지지 않으면
        print('Bye')    # Bye를 출력하고
    else:               # 나눠 떨어지면
        print('Good')   # Good을 출력한다