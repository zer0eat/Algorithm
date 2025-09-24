# 선택 가능성이 가장 높은 자료형_BOJ32278

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                            # 숫자를 input받고
if -32768 <= N and N <= 32767:              # 숫자의 범위가 포함된다면
    print('short')                          # short 자료형을 출력하고
elif -2147483648 <= N and N <= 2147483647:  # short보다는 크지만 숫자의 범위가 포함된다면
    print('int')                            # int 자료형을 출력하고
else:                                       # 모두 초과한다면
    print('long long')                      # long long 자료형을 출력한다