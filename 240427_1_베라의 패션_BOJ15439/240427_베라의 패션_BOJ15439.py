# 베라의 패션_BOJ15439

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 상하의의 종류를 input 받고
print(N*(N-1))      # 상의와 하의가 서로 다른 색상의 조합의 수를 출력한다