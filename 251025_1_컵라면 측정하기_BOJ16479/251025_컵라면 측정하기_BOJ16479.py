# 컵라면 측정하기_BOJ16479

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
K = int(input())                    # 컵라면의 빗변의 길이를 input받고
D1, D2 = map(int, input().split())  # 컵라면의 위 아래 지름의 길이를 input받고
print(K**2-((D1/2)-(D2/2))**2)      # 컵라면의 높이의 제곱값을 출력한다