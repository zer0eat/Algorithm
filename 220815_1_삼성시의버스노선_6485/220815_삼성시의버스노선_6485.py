# 삼성시의 버스노선_6485

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    N = int(input()) # 버스 노선의 수
    bus_route = [] # 버스가 서는 정류장
    for n in range(N):
        S, N = input().split()
        S = int(S) # 노선의 시작점
        N = int(N) # 노선의 종점
        bus_route.append(range(S, N + 1)) # 노선의 시작부터 종점까지 범위로 버스 노선 저장

    P = int(input()) # 버스 정류장의 수
    bus_stop = []  # 정류장 번호
    for p in range(P):
        bus_stop.append(int(input()))

    bus_stop_cnt = [] # 정류장 마다 버스가 정차하는 횟수
    # 각각의 정류장마다
    for b in bus_stop:
        cnt = 0
        # 각 노선의 버스가 정차한다면 cnt를 1 추가하고
        for bus in bus_route:
            if b in bus:
                cnt += 1
        # 모든 노선을 확인 후 bus_stop_cnt에 최종 정차 횟수를 저장
        else:
            bus_stop_cnt.append(cnt)

    print(f'#{t+1}', *bus_stop_cnt)
