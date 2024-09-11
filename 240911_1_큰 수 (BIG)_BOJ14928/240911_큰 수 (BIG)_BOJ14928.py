# 큰 수 (BIG)_BOJ14928

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 큰 수를 input 받고
print(N % 20000303) # 20000303로 나눈 나머지를 출력한다