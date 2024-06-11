# 240611_1_A+B-C_BOJ31403

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = int(input())            # 정수 A를 input 받고
B = int(input())            # 정수 B를 input 받고
C = int(input())            # 정수 C를 input 받고
print(A+B-C)                # A, B, C를 수로 생각했을 때, A+B-C를 출력하고
print(int(str(A)+str(B))-C) # A, B, C를 문자로 생각했을 때, A+B-C를 출력한다