# 미국 스타일_BOJ2712

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                                # 테스트 케이스를 input받고
for t in range(T):                              # 테스트 케이스를 반복해서
    A = list(input().split())                   # 숫자와 단위를 input받고
    if A[1] == 'kg':                            # 킬로그램으로 나왔다면
        print(f'{float(A[0])*2.2046:.4f} lb')   # 파운드로 변환해서 출력하고
    elif A[1] == 'l':                           # 리터로 나왔다면
        print(f'{float(A[0])*0.2642:.4f} g')    # 갤런으로 바꿔서 출력하고
    elif A[1] == 'lb':                          # 파운드로 나왔다면
        print(f'{float(A[0])*0.4536:.4f} kg')   # 킬로그램으로 바꿔서 출력하고
    elif A[1] == 'g':                           # 갤런으로 나왔다면
        print(f'{float(A[0])*3.7854:.4f} l')    # 리터로 바꿔서 출력한다