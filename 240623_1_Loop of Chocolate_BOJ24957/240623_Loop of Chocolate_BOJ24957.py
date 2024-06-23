# Loop of Chocolate_BOJ24957

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

# input 받기
N, R = map(int, input().split())                        # 구의 개수와 반지름의 길이를 input 받고
C = [list(map(int, input().split())) for _ in range(N)] # 구의 중점을 리스트로 input 받는다
V = (4/3) * math.pi * R**3                              # 한개의 구의 부피를 구하고
ans = N * V                                             # N개의 구의 부피의 합을 변수에 저장한다
for n in range(N):                                      # 구의 개수를 반복해서
    if n == N-1:                                        # 마지막 구라면
        d = ((C[n][0]-C[0][0])**2 + (C[n][1]-C[0][1])**2 + (C[n][2]-C[0][2])**2)**(1/2)         # n번과 n+1번 구의 거리를 구하고
    else:                                               # 마지막 구가 아니라면
        d = ((C[n][0]-C[n+1][0])**2 + (C[n][1]-C[n+1][1])**2 + (C[n][2]-C[n+1][2])**2)**(1/2)   # 첫번째와 마지막 구의 거리를 구하고
    ans -= (2/3)*math.pi*((R-(d/2))**2)*(2*R+(d/2))     # 전체 부피에서 겹치는 구의 부피를 빼준다
print(ans)                                              # 전체의 부피를 출력한다