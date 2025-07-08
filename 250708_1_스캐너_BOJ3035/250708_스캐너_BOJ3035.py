# 스캐너_BOJ3035

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
R, C, ZR, ZC = map(int, input().split())    # 그림의 크기와 확대할 크기를 input받고
for r in range(R):                          # 그림의 행을 반복해서
    S = input().strip()                     # 한행을 input받고
    for zr in range(ZR):                    # 확대할 행을 반복해서
        for c in range(C):                  # 그림의 열을 반복해서
            if c == C-1:                    # 마지막 열이면
                print(S[c]*ZC)              # 출력하고 줄을 바꾸고
            else:                           # 마지막 열이 아니라면
                print(S[c]*ZC, end='')      # 출력하고 줄을 바꾸지 않는다