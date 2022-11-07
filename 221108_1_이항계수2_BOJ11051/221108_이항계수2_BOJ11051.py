# 이항계수2_BOJ11051

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
N, K = map(int, sys.stdin.readline().split())   # 자연수 N과 정수 K를 받는다

cnt = 1                                         # 계산결과를 저장할 변수를 생성하고
for i in range(N, N-K, -1):                     # N부터 1씩 작아지는 K개의 정수를 반복해서
    cnt *= i                                    # cnt에 곱해주고
for j in range(1, K+1):                         # 1부터 1씩 증가하는 K개의 정수를 반복해서
    cnt //= j                                   # cnt에 나눠준다

print(cnt % 10007)                              # 10007로 나눈 나머지를 출력한다