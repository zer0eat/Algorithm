# 제곱근_BOJ13706

# import.txt 열기
import sys
sys.stdin = open('input.txt')
from math import isqrt

# input 받기
N = int(sys.stdin.readline())   # 정수 N을 input 받아서
print(isqrt(N))                 # N의 제곱근을 출력한다