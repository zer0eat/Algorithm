# SASA 모형을 만들어보자_BOJ23825

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())    # S와 A의 개수를 input 받고
print(min(N//2, M//2))              # SASA를 만들 수 있는 개수를 출력한다