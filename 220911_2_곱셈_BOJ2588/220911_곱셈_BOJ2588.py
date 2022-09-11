# 곱셈_BOJ2588

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
A = int(input())                # 세자리 수 자연수 input
B = int(input())                # 세자리 수 자연수 input

print(A*(B%10))                 # A X B의 일의자리 수의 곱
print(A*((B//10)%10))           # A X B의 십의자리 수의 곱
print(A*(((B//10)//10)%10))     # A X B의 백의자리 수의 곱
print(A*B)                      # A X B