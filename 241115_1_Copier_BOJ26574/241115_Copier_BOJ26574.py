# Copier_BOJ26574

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 숫자의 개수를 input 받고
for n in range(N):      # 숫자의 개수를 반복해서
    M = int(input())    # 숫자를 input 받고
    print(M, M)         # 숫자를 반복해서 출력한다