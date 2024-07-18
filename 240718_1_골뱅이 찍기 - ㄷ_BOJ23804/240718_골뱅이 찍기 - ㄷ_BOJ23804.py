# 골뱅이 찍기 - ㄷ_BOJ23804

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())        # 셀의 크기를 input 받고 
for n in range(N):      # N줄 반복해서
    print('@@@@@'*N)    # ㄷ의 상단을 출력하고
for n in range(3*N):    # 3N줄 반복해서
    print('@'*N)        # ㄷ의 중단을 출력하고
for n in range(N):      # N줄 반복해서
    print('@@@@@'*N)    # ㄷ의 하단을 출력한다