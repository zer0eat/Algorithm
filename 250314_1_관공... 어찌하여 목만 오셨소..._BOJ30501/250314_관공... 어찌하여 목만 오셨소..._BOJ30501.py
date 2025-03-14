# 관공... 어찌하여 목만 오셨소..._BOJ30501

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())            # 용의자 수를 input 받고
for n in range(N):          # 용의자를 반복해서
    name = input().strip()  # 용의자의 이름을 input 받고
    if 'S' in name:         # 이름에 S가 들어가면
        print(name)         # 용의자를 출력하고
        quit()              # 종료한다