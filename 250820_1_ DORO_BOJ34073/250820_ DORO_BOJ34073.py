# DORO_BOJ34073

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                # 단어의 수를 input받고
W = list(input().split())       # 단어를 리스트로 input받고
for w in W:                     # 단어를 반복해서
    print(w+'DORO', end=' ')    # 단어의 마지막에 DORO를 붙여서 출력한다