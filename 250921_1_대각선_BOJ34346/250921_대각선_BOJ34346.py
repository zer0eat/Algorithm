# 대각선_BOJ34346

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 숫자를 input받고
if N % 2:           # 한 행이 홀수라면
    print(1)        # 칠해야하는 칸을 1로 출력하고
else:               # 한 행이 짝수라면
    print(2)        # 칠해야하는 칸을 2로 출력한다