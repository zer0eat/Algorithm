# Just Round Down_BOJ32458

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = float(input())  # 실수를 input 받고
print(int(N))       # 정수부분만 출력한다