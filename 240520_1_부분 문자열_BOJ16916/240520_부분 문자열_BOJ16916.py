# 부분 문자열_BOJ16916

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
S = input().strip()     # 문자열을 input 받고
P = input().strip()     # 부분문자열을 input 받고
if P in S:              # 부분문자열이 문자열에 포함되면
    print(1)            # 1을 출력하고
else:                   # 그렇지 않다면
    print(0)            # 0을 출력한다