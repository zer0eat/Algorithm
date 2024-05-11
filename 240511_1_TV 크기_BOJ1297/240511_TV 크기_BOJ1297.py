# TV 크기_BOJ1297

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
D, H, W = map(int, input().split()) # D 대각선의 길이 / H 높이의 비율 / W 너비의 비율을 input 받고
ans = D / (H**2+W**2)**0.5          # H와 W의 최대공약수를 구한다
print(int(H*ans), int(W*ans))       # 높이와 너비의 원래 크기를 소수점 없이 출력한다