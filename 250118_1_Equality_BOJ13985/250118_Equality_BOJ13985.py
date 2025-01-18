# Equality_BOJ13985

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
form = list(input().split())                    # 수식을 input 받고
if int(form[0]) + int(form[2]) == int(form[4]): # 수식이 맞다면
    print('YES')                                # YES를 출력하고
else:                                           # 틀리다면
    print("NO")                                 # NO를 출력한다