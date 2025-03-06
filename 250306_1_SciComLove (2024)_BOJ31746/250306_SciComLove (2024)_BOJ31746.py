# SciComLove (2024)_BOJ31746

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 숫자를 input 받고
if N % 2:               # 뒤집을 숫자가 홀수라면
    print('evoLmoCicS') # 뒤집어서 출력하고
else:                   # 뒤집을 숫자가 짝수라면
    print('SciComLove') # 그대로를 출력한다