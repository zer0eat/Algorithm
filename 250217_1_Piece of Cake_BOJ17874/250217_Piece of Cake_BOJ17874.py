# Piece of Cake_BOJ17874

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
n, h, v = map(int, input().split()) # 케이크의 크기와 자른 부분을 input 받고
print(4*max(n-h, h)*max(n-v,v))     # 가장 큰 케이크의 부피를 출력한다