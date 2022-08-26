# 새로운버스노선_13994

# input.txt 열기
import sys
sys.stdin =open('input.txt')

# input 받기
T = int(input())
for t in range(T):                                                  # 테스트 케이스
    N = int(input())                                                # 버스 노선의 수
    bus = [list(map(int, input().split())) for _ in range(N)]       # 인덱스 : 0번 = 1 일반, 2 급행, 3 광역 / 1번 출발정류장 / 2번 도착 정류장

    # 버스가 정차하는 정류장 만들기
    far = 0                                                         # 가장 먼 버스정류장의 번호
    for i in range(len(bus)):                                       # 버스의 정보를 반복해서
        if bus[i][2] > far:                                         # 도착지의 번호가 far보다 먼 경우
            far = bus[i][2]                                         # 도착지를 far에 저장한다.

    bus_stop = [0] * (far + 1)                                      # 가장 먼 도착지가 인덱스가 되도록 빈 리스트를 만들어 준 후

    # 버스가 정차하는 정류장 표시하기
    for b in bus:                                                   # 버스의 정보를 반복해서
        # 일반버스
        if b[0] == 1:                                               # 0번 인덱스가 1이면 일반버스이므로
            for q in range(b[1], b[2]+1):                           # 출발지부터 도착지까지
                bus_stop[q] += 1                                    # 모든 정류장에 정차한다
        # 급행버스
        elif b[0] == 2:                                             # 1번 인덱스가 2이면 급행버스이므로
            # 출발지가 짝수 일 때 짝수 번째만 정차
            if b[1] % 2 == 0:
                for w in range(b[1], b[2]+1):
                    if w % 2 == 0:
                        bus_stop[w] += 1
            # 출발지가 홀수 일 때 홀수 번째만 정차
            elif b[1] % 2 == 1:
                for w in range(b[1], b[2]+1):
                    if w % 2 == 1:
                        bus_stop[w] += 1
        # 광역버스
        elif b[0] == 3:                                             # 1번 인덱스가 3이면 광역버스이므로
            # 출발지가 짝수 일 때 4의 배수의 번호에 정차
            if b[1] % 2 == 0:
                for w in range(b[1], b[2]+1):
                    if w % 4 == 0:
                        bus_stop[w] += 1
            # 출발지가 홀수 일 때 3의배수의 번호에는 정차하고 10의 배수 번호에는 정차하지 않는다
            elif b[1] % 2 == 1:
                for w in range(b[1], b[2]+1):
                    if w % 3 == 0 and w % 10 != 0:
                        bus_stop[w] += 1

    # 가장 많이 정차하는 정류장의 버스의 수
    many_stop = 0
    for u in bus_stop:
        if many_stop < u:
            many_stop = u

    print(f'#{t+1}', many_stop)