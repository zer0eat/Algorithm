# 4-LSB_BOJ32685

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = bin(int(input()))                   # A를 2진수로 input 받고
A = '0000'+A[2:]                        # 이진수의 앞을 0000으로 변환한다
B = bin(int(input()))                   # B를 2진수로 input 받고
B = '0000'+B[2:]                        # 이진수의 앞을 0000으로 변환한다
C = bin(int(input()))                   # C를 2진수로 input 받고
C = '0000'+C[2:]                        # 이진수의 앞을 0000으로 변환한다
ans = int(A[-4:]+B[-4:]+C[-4:],2)       # 이진수의 마지막 4자리의 합을 10진수로 변환하고
print('0'*(4-len(str(ans)))+str(ans))   # 4자리의 10진수를 출력한다