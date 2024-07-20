# 헛간 청약_BOJ19698

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, H, W, L = map(int, input().split())  # N 소의 수 / H 세로의 크기 / W 가로의 크기 / L 방한칸의 가로 세로 넓이를 input 받고
H = H // L                              # 세로에 L크기의 방이 들어갈 수 있는 수를 구하고
W = W // L                              # 가로에 L크기의 방이 들어갈 수 있는 수를 구해서
print(min(N, H*W))                      # 방의 최대수와 소의 수 중 작은 값을 출력하여 입주할 수 있는 수를 출력한다