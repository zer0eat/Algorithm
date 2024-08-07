# 치킨 두 마리 (...)_BOJ14489

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())    # 두 통장의 잔고를 input 받고
C = int(input())                    # 치킨 한마리 값을 input 받아서
if A+B-(C*2) >= 0:                  # 잔고로 치킨 2마리를 살 수 있다면
    print(A+B-(C*2))                # 사고 남은 차액을 출력하고
else:                               # 잔고로 치킨 2마리를 살 수 없다면
    print(A+B)                      # 잔고를 출력한다