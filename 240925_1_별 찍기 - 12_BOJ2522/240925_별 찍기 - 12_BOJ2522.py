# 별 찍기 - 12_BOJ2522

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # 별의 최대 개수를 input 받고
for n in range(1, N+1):     # 별의 개수를 1부터 N까지 반복해서
    print(' '*(N-n)+'*'*n)  # n개의 별을 출력하고
for n in range(N-1, 0, -1): # 별의 개수를 N-1부터 1까지 반복해서
    print(' '*(N-n)+'*'*n)  # N-n개의 별을 출력한다