# 배수와약수_BOJ5086

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
while 1:                                            # break가 나올때까지 while문을 반복해서
    A, B = map(int, sys.stdin.readline().split())   # A와 B에 각각 자연수를 input 받는다
    if A == 0 and B == 0:                           # A와 B 모두 0이라면
        break                                       # break
    elif A % B == 0:                                # A가 B의 배수라면
        print('multiple')                           # multiple
    elif B % A == 0:                                # B가 A의 배수라면
        print('factor')                             # factor
    else:                                           # 모두 아니라면
        print('neither')                            # neither를 출력한다

