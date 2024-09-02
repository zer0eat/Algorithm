# 이제는 더 이상 물러날 곳이 없다_BOJ30455

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())    # 전장의 길이를 input 받고
if N % 2:           # 전장의 길이가 홀수라면
    print('Goose')  # 건구스의 승리를 출력하고
else:               # 전장의 길이가 짝수라면
    print('Duck')   # 건덕의 승리를 출력한다