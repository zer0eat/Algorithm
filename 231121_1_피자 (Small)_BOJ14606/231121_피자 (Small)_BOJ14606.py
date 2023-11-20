# 피자 (Small)_BOJ14606

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 피자판의 수를 input 받고
print(N*(N-1)//2)   # 얻을 수 있는 즐거움의 총합의 최댓값을 출력한다