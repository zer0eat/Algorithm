# 홀수일까 짝수일까_BOJ5988

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 숫자의 개수를 input 받고
for n in range(N):      # 숫자의 개수를 반복해서
    num = int(input())  # 숫자를 input 받고
    if num%2:           # 숫자가 홀수라면
        print('odd')    # odd를 출력하고
    else:               # 숫자가 짝수라면
        print('even')   # even을 출력한다