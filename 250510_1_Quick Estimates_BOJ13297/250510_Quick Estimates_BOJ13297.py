# Quick Estimates_BOJ13297

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 작업자의 수를 input받고
for n in range(N):                      # 작업자의 수를 반복해서
    print(len(list(input().strip())))   # 작업자에게 줘야하는 달러의 자리수를 출력한다