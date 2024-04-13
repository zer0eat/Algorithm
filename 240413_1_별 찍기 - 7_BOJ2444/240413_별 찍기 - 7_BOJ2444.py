# 별 찍기 - 7_BOJ2444

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 별을 찍기 위한 줄을 input 받고
for i in range(1, N):               # 별을 찍을 줄을 증가하는 만큼 반복해서
    print(' '*(N-i) + '*'*(2*i-1))  # 증가하는 별을 출력한다
for i in range(N, 0, -1):           # 별을 찍을 줄을 감소하는 만큼 반복해서
    print(' '*(N-i) + '*'*(2*i-1))  # 감소하는 별을 출력한다