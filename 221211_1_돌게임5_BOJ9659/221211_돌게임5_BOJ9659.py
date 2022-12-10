# 돌게임5_BOJ9659

# import.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(sys.stdin.readline())   # 돌의 개수

if N % 2:                       # 돌의 개수가 홀수이면
    print('SK')                 # SK를 출력하고
else:                           # 돌의 개수가 짝수이면
    print('CY')                 # CY를 출력한다