# ブラックジャック (Blackjack)_BOJ33170

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A = int(input())    # 숫자 A를 input 받고
B = int(input())    # 숫자 B를 input 받고
C = int(input())    # 숫자 C를 input 받고
if A+B+C <= 21:     # 세 수의 합이 21 이하라면
    print(1)        # 1을 출력하고
else:               # 세 수의 합이 22 이상이라면
    print(0)        # 0을 출력한다