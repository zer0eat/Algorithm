# 알약_BOJ4811

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
pills = [[0] * 31 for _ in range(31)]                   # 약을 먹는 방법을 저장할 행렬을 생성하고
for k in range(1, 31):                                  # 1부터 30까지 반복해서
    pills[0][k] = 1                                     # 첫날 한 조각을 꺼내는 경우의 수를 모두 1로 저장한다
for i in range(1, 31):                                  # 반 조각을 꺼내는 경우를 1부터 30까지 반복하고
    for j in range(i, 31):                              # 한 조각을 꺼내는 경우를 1부터 30까지 반복해서
        pills[i][j] += pills[i-1][j] + pills[i][j-1]    # i개의 반조각과 j개의 한조각으로 만드는 경우의 수를 반조각 i-1 / 한조각 j 의 경우의 수와 반조각 i / 한조각 j-1 의 경우의 수의 합으로 저장한다
while 1:                                                # break가 나올때까지 반복해서
    N = int(input())                                    # 약의 개수를 input 받고
    if N == 0:                                          # 약의 개수가 0이라면
        break                                           # while문을 break 한다
    print(pills[N][N])                                  # 약의 개수가 0이 아니라면 가능한 문자열의 개수를 출력한다