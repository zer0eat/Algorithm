# 공백없는 A+B_BOJ15873

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = input().strip()                 # 숫자를 input 받고
if N[1] == '0':                     # 두번쨰 숫자가 0이라면
    print(10 + int(N[2:]))          # 10과 나머지 숫자를 더해 출력하고
else:                               # 두번째 숫자가 0이 아니라면
    print(int(N[0]) + int(N[1:]))   # 두 숫자를 더해 출력한다