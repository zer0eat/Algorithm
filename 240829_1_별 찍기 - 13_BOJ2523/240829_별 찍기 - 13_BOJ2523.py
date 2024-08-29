# 별 찍기 - 13_BOJ2523

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # 별을 출력할 줄을 input 받고
for n in range(1, N+1):     # 1부터 N까지 반복하면
    print('*'*n)            # n개의 별을 출력하고
for n in range(N-1, 0, -1): # N-1부터 1까지 반복하며
    print('*'*n)            # n개의 별을 출력한다