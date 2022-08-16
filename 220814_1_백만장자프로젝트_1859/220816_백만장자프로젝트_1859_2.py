# 백만장자프로젝트_1859_슬라이싱 없애기

# input.txt 열기
import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스
for t in range(T):
    N = int(input()) # N = 원료를 거래하는 날
    lst = list(map(int, input().split())) # n일차 원료의 가격을 담은 리스트

    # 구매하고 판매하기
    maxP = lst[-1] # 판매할 최고가격을 마지막날 가격으로 잡고 시작
    p = 0 # 판매 이익
    c = 0 # 구입 개수
    o = 0 # 구입 비용

    # 구매가격을 거래일 마지막부터 첫째날까지 반복
    for n in range(len(lst)-1, -1, -1):
        # 현재 최고가보다 더 비싼가격이 나온다면
        if maxP < lst[n]:
            # 이익정산 = 최대가격*구매개수-구입비용
            p += maxP * c - o
            # 최고가 가격을 다시 설정
            maxP = lst[n]
            # 구입 개수와 비용을 초기화
            c = 0
            o = 0
        # 현재 가격보다 낮은가격이 나온다면
        elif maxP >= lst[n]:
            # 1개를 구매하고, 구입비용에 1개를 구입하는데 든 비용을 추가
            c += 1
            o += lst[n]
    # 첫째날까지 반복을 완료했다면
    else:
        # 이익정산 = 최대가격*구매개수-구입비용
        p += maxP * c - o

    print(f'#{t+1}', p)