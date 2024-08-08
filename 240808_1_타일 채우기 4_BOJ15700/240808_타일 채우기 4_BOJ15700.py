# 타일 채우기 4_BOJ15700

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M = map(int, input().split())                                # 벽의 가로와 세로의 크기를 input 받고
print(max((M//2)*N + (M%2)*(N//2), (N//2)*M + (N%2)*(M//2)))    # 1X2부터 채울 수 있는 개수와 2X1부터 채울 수 있는 개수 중 더 큰 값을 출력한다