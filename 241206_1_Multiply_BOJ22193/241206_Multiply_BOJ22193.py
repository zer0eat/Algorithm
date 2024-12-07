# Multiply_BOJ22193

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # A와 B의 자리수를 input 받고
A = int(input())                    # A를 input 받고
B = int(input())                    # B를 input 받고
print(A*B)                          # A*B를 출력한다