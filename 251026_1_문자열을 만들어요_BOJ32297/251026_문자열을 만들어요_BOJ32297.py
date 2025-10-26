# 문자열을 만들어요_BOJ32297

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 문자열의 길이를 input받고
S = input().strip() # 문자열을 input받고
if 'gori' in S:     # gori가 문자열에 포함된다면
    print('YES')    # 예를 출력하고
else:               # 포함되지 않는다면
    print('NO')     # 아니오를 출력한다