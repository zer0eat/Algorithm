# 백대열_BOJ14490

# input.txt 열기
import sys
sys.stdin = open('input.txt')
import math

# input 받기
A = list(map(int, sys.stdin.readline().split(':')))     # ':' 를 기준으로 앞뒤 숫자를 리스트로 input 받고
B = math.gcd(A[0], A[1])                                # A에 있는 두 수의 최대공약수를 구해서 B에 저장한 후
print(f'{A[0]//B}:{A[1]//B}')                           # A[0]과 A[1]를 최대공약수로 약분한 수를 비율로 출력한다