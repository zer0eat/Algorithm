# 알고리즘 수업 - 점근적 표기 1_BOJ24313

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
a1, a0 = map(int, input().split())  # f(n)의 계수 a1과 상수항 a0를 input 받고
c = int(input())                    # g(n)의 상수항 c를 input 받고
n0 = int(input())                   # 기준이 되는 n 값을 n0로 input 받고
if a1*n0+a0 <= c*n0 and a1 <= c:    # n ≥ n0, f(n) ≤ c × g(n)인 조건을 만족한다면
    print(1)                        # 1을 출력하고
else:                               # 조건을 만족하지 못한다면
    print(0)                        # 0을 출력한다