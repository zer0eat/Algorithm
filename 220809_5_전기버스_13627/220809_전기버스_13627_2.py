# 전기버스_13627

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 리스트로 받기
T = int(input())
for t in range(T):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))

    # 정류장과 충전기 리스트 만들기
    busstop = [0] * N
    for cha in charger:
        busstop[cha] += 1

    # 충전 횟수 세기
    cnt = 0 # 충전 횟수
    bus = 0 # 버스위치
    charge = 0  # 가까운 충전소
    move = 0  # 이동거리

    # 버스위치 + 이동거리가 전체 정류장 수보다 크기가 작을때
    while bus + move < N:
        # 충전소가 있는 정류장을 만나면 위치를 charge에 저장
        if busstop[bus + move] == 1:
            charge = bus + move

        # 최대 이동거리 K만큼 이동했을 때
        if K - move == 0:
            # 충전소를 만나지 못했으면 break
            if bus == charge:
                cnt = 0
                break
            # 충전소를 만났으면 bus를 charge 위치에서 다시 출발
            else:
                bus = charge
                move = 0
                cnt += 1
        # 한정거장 이동
        move += 1
    print(f'#{t + 1} {cnt}')