# 250828_루트_BOJ4619

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

# input 받기
while 1:                                    # break가 나올때까지 반복해서
    B, N = map(int, input().split())        # B와 제곱수를 Input받고
    if B == 0 and N == 0:                   # 둘다 0이라면
        break                               # while문을 종료한다
    A = B**(1/N)                            # A를 구해서
    n, m = math.floor(A), math.ceil(A)      # A를 내린수를 n A를 올린 수를 m으로 저장하고
    if abs(B-n**N) < abs(B-m**N):           # n이 B와 더 가깝다면
        print(n)                            # n을 출력하고
    else:                                   # m이 B와 더 가깝다면
        print(m)                            # m을 출력한다