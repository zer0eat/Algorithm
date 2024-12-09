# UOS 문자열_BOJ32929

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
x = int(input())    # 순서를 input 받고
x %= 3              # 3을 나눈 나머지를 구해서
if x == 1:          # 나머지가 1이라면
    print('U')      # U를 출력한다
elif x == 2:        # 나머지가 2라면
    print('O')      # O를 출력한다
else:               # 나머지가 0이라면
    print('S')      # S를 출력한다