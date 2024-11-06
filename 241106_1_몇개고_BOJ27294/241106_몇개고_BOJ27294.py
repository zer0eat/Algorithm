# 몇개고_BOJ27294

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T, S = map(int, input().split())    # 식사 시간과 음주 여부를 input 받고
if 12 <= T and T <= 16 and S == 0:  # 점심시간에 술을 마시지 않는다면
    print(320)                      # 320알을 출력하고
else:                               # 그 외에는
    print(280)                      # 280알을 출력한다