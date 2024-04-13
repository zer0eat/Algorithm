# 별 찍기 - 7_BOJ2444

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())
for i in range(1, N):
    print(' '*(N-i) + '*'*(2*i-1))
for i in range(N, 0, -1):
    print(' '*(N-i) + '*'*(2*i-1))