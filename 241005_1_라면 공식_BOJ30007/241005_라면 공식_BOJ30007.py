# 라면 공식_BOJ30007

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 라면 끓이는 수를 input 받고
for n in range(N):                      # 라면 끓이는 수를 반복해서
    A, B, X = map(int, input().split()) # A 라면의 계수 B 기본 물의양 X 라면의 개수를 input 받고
    print(A*(X-1)+B)                    # 라면을 끓일 때 필요한 물의 양을 출력한다