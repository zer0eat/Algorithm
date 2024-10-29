# Rectangles_BOJ15232

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
R = int(input())    # 세로의 길이를 input 받고
C = int(input())    # 가로의 길이를 input 받고
for r in range(R):  # 세로의 길이를 반복해서
    print('*'*C)    # 가로의 길이만큼 *을 출력한다