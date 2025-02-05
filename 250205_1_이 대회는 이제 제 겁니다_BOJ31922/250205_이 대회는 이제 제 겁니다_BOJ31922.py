# 이 대회는 이제 제 겁니다_BOJ31922

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, P, C = map(int, input().split()) # 디비전 1, 2, 3 상금을 input 받고
if A+C > P:                         # 1, 3 우승 상금이 더 크면
    print(A+C)                      # 1, 3 우승 상금의 합을 출력하고
else:                               # 2 우승 상금이 더 크면
    print(P)                        # 2 우승 상금을 출력한다