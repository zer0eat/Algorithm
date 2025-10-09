# 앵그리 창영_BOJ3034

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, W, H = map(int, input().split()) # 성냥의 수와 가로 세로의 크기를 input받고
ans = (W**2 + H**2)**(0.5)          # 대각선의 길이를 구해서
for n in range(N):                  # 성냥의 크기를 반복해서
    if int(input()) <= ans:         # 성냥이 들어갈 수 있으면 
        print('DA')                 # DA를 출력하고
    else:                           # 성냥이 들어갈 수 없으면 
        print('NE')                 # NE를 출력한다