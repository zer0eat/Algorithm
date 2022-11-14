# 링_BOJ3036

# import.txt 열기
import sys
sys.stdin = open('input.txt')
from fractions import Fraction

# input 받기
N = int(sys.stdin.readline())                       # 링의 개수를 input 받고
lst = list(map(int, sys.stdin.readline().split()))  # 링의 크기를 list에 저장한다

for n in range(N):                                  # 링의 개수만큼 반복해서
    if n == 0:                                      # 첫번째 링이면
        A = lst[n]                                  # A에 그 크기를 저장하고
    else:                                           # 첫번째 링이 아니라면
        if A / lst[n] == A // lst[n]:               # 첫번째 링을 다른 링으로 나눴을 때 딱 나눠 떨어진다면
            print(f'{A // lst[n]}/1')               # 기약분수 형태로 분모가 1인 형식으로 출력한다
        else:                                       # 만약 나눠떨어지지 않는다면
            print(Fraction(A, lst[n]))              # 기약분수 형태로 출력한다