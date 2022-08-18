# 두개의 숫자열_1959

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())         # 테스트 케이스
for t in range(T):
    N, M = map(int, input().split())
    print(N,M)

    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    print(Ai, Bj)