# 전기버스_13627

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 리스트로 받기
T = int(input()) #테스트 케이스
for t in range(T):
    K, N, M = map(int,input().split()) # K는 버스가 이동할수 있는 거리 N은 정류장의 개수 M은 충전기의 개수
    charger = list(map(int, input().split()))

    # 정류장과 충전기 리스트 만들기
    busstop = [0] * N
    for cha in charger:
        busstop[cha] += 1

    # 충전 횟수 세기
    cnt = 0
    bus = 0
    while bus + K < N:
        for k in range(K, 0, -1):
            if busstop[bus + k] == 1:
                bus = bus + k
                cnt += 1
                break

        else:
            cnt = 0
            break
    print(f'#{t+1} {cnt}')
