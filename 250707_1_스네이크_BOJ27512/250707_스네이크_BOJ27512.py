# 스네이크_BOJ27512

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
n, m = map(int, input().split())    # 가로와 세로의 길이를 input받고
if n%2 and m%2:                     # 두 길이 모두 홀수라면
    print(n*m-1)                    # 모든 칸에서 한칸을 뺀 값을 출력하고
else:                               # 하나라도 짝수라면
    print(n*m)                      # 모든 칸의 값을 출력한다