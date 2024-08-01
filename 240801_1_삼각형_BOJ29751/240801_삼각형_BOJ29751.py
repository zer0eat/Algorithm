# 삼각형_BOJ29751

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
W, H = map(int, input().split())    # 삼각형의 밑변과 높이의 길이를 input 받고
print(round(W*H/2, 1))              # 삼각형의 넓이를 소수 첫 번째 자리까지 출력한다