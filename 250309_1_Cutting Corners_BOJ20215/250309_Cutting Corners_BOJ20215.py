# Cutting Corners_BOJ20215

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
w, h = map(int, input().split())    # 가로와 세로를 input 받고
ans = w+h - (w**2 + h**2)**0.5      # 가로와 세로로 짜르는 것보다 대각선으로 짜르면 얼마나 차이가 나는지 구해서
print(ans)                          # 출력한다