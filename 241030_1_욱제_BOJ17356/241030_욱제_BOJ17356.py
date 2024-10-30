# 욱제_BOJ17356

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())    # A, B의 욱제력을 input 받고
M = (B-A)/400                       # M을 구해 저장한다
print(1/(1+10**M))                  # 욱이 제를 이길 확률을 출력한다