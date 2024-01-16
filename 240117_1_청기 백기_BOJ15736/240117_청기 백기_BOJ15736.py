# 청기 백기_BOJ15736

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # 깃발의 개수를 input 받고
print(int(N**0.5))          # 백색인 깃발의 수를 출력한다