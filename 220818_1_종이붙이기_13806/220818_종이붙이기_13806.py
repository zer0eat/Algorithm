# 종이붙이기_13806

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())            # 테스트케이스
for t in range(T):
    N = int(input())        # 가로의 길이
    while N > 0:
        if N / 20 != 0:
