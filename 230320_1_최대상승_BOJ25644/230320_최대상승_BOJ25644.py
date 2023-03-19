# 최대상승_BOJ25644

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # N ANA의 주가를 예측 가능한 날
ANA = list(map(int, input().split()))   # N일간의 ANA의 주가를 리스트로 input
ans = 0                                 # 최대 수익을 저장할 변수 생성
maxprice = ANA[-1]                      # 최대금액을 저장할 변수를 생성하고 마지막날 가격으로 저장
for p in range(N-2, -1, -1):            # 마지막날 하루 전부터 처음까지 반복해서
    if ANA[p] > maxprice:               # p일의 금액이 현재 최대금액보다 크다면
        maxprice = ANA[p]               # maxprice를 p일의 금액으로 변경한다
    elif ANA[p] < maxprice:             # p일의 금액이 현재 최대금액보다 작다면
        if (maxprice - ANA[p]) > ans:   # 현재 저장된 최대 수익보다 최대금액에서 p일 까지의 수익이 더 클 때
            ans = (maxprice - ANA[p])   # 최대 수익을 최대금액에서 p일 까지의 수익으로 변경한다
else:                                   # 모든 날을 반복했다면
    print(ans)                          # 최대 수익 날을 출력한다