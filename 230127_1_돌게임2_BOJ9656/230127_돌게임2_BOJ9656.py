# 돌게임2_BOJ9656

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())    # 돌의 개수

if N % 2:           # 돌이 짝수라면
    print('CY')     # 창영이의 승리
else:               # 돌이 홀수라면
    print('SK')     # 상근이의 승리