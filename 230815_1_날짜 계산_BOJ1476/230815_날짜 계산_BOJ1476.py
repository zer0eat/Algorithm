# 날짜 계산_BOJ1476

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
E, S, M = map(int, input().split())     # E 지구를 나타내는 수 / S 태양을 나타내는 수 / M 달을 나타내는 수
N = S                                   # 우리가 알고 있는 연도를 태양을 나타내는 수로 저장하고
if E == 15:                             # 지구를 나타내는 수가 15라면
    E = 0                               # 0으로 저장하고
if S == 28:                             # 태양를 나타내는 수가 28이라면
    S = 0                               # 0으로 저장하고
if M == 19:                             # 달을 나타내는 수가 19라면
    M = 0                               # 0으로 저장한다
while 1:                                # break가 나올때까지 반복해서
        if N % 19 == M:                 # 우리가 알고 있는 연도를 19로 나눴을 때 달을 나타내는 수라면
            if N % 15 == E:             # 우리가 알고 있는 연도를 15로 나눴을 때 지구를 나타내는 수라면
                print(N)                # 우리가 알고 있는 가장 빠른 연도를 출력하고
                break                   # while문을 break한다
            else:                       # 지구를 나타내는 수가 아니라면
                N += 28                 # 태양의 최대 범위 만큼 더해준다
        else:                           # 달을 나타내는 수가 아니라면
            N += 28                     # 태양의 최대 범위 만큼 더해준다