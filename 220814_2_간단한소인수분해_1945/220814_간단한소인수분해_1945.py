# 간단한소인수분해_1945

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    N = int(input())

    a = 0 # 2로 나눈 횟수
    b = 0 # 3으로 나눈 횟수
    c = 0 # 5로 나눈 횟수
    d = 0 # 7로 나눈 횟수
    e = 0 # 11로 나눈 횟수

    while N > 1:
        if N % 2 == 0:
            N = N/2
            a += 1
        elif N % 3 == 0:
            N = N/3
            b += 1
        elif N % 5 == 0:
            N = N/5
            c += 1
        elif N % 7 == 0:
            N = N/7
            d += 1
        elif N % 11 == 0:
            N = N/11
            e += 1
    print(f'#{t+1}', a,b,c,d,e)