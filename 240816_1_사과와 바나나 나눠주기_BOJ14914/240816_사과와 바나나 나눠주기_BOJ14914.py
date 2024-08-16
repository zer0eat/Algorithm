# 사과와 바나나 나눠주기_BOJ14914

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
a, b = map(int, input().split())    # 사과와 바나나의 수를 input 받고
N = min(a, b)                       # 두 과일 중 작은 수를 저장한다
for n in range(1, N+1):             # 1부터 작은과일의 수까지 반복해서
    if a % n == 0 and b % n == 0:   # n명에게 똑같이 나누어 줄 수 있다면
        print(n, a//n, b//n)        # n명, 나눠줄 사과의 수, 나눠줄 바나나의 수를 출력한다