# Lunacy_BOJ4714

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
while 1:                # break가 나올 때까지 반복해서
    N = float(input())  # 숫자를 input 받고
    if N == -1:         # -1이 나왔다면
        break           # while문을 종료하고고
    print(f'Objects weighing {N:.2f} on Earth will weigh {N*0.167:.2f} on the moon.') # -1이 아니라면 달에서 무게를 출력한다