# 백만장자프로젝트_1859

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    N = int(input()) # N = 원료를 거래하는 날
    lst = list(map(int, input().split()))[::-1] # n일차 원료의 가격을 담은 리스트를 마지막날 순서부터 정렬

    # 구매하고 판매하기
    max_price = lst[0] # 판매할 최고가격을 마지막날 가격으로 잡고 시작
    profit = 0 # 판매 이익
    cnt = 0 # 구입 개수
    cost = 0 # 구입 비용

    # 구매가격을 거래일 마지막부터 첫째날까지 반복
    for n in range(1, N):
        # 현재 최고가보다 더 비싼가격이 나온다면
        if max_price < lst[n]:
            # 이익정산 = 최대가격*구매개수-구입비용
            profit += max_price * cnt - cost
            # 최고가 가격을 다시 설정
            max_price = lst[n]
            # 구입 개수와 비용을 초기화
            cnt = 0
            cost = 0
        # 현재 가격보다 낮은가격이 나온다면
        elif max_price >= lst[n]:
            # 1개를 구매하고, 구입비용에 1개를 구입하는데 든 비용을 추가
            cnt += 1
            cost += lst[n]
    # 첫째날까지 반복을 완료했다면
    else:
        # 이익정산 = 최대가격*구매개수-구입비용
        profit += max_price * cnt - cost

    print(f'#{t+1}', profit)