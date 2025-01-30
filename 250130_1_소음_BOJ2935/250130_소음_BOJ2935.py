# 소음_BOJ2935

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = int(input())    # 숫자를 input 받고
C = input().strip() # 계산자를 input 받고
B= int(input())     # 숫자를 input 받아서
if C == '*':        # 계산자가 곱하기라면
    print(A*B)      # 두 수를 곱한 값을 출력하고
else:               # 계산자가 더하기라면
    print(A+B)      # 두 수를 더한 값을 출력한다