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
    cnt = 0
    bus = 0
    while bus + K < N:
        for k in range(K):
            if busstop[bus + K - k] == 1:
                bus = bus + K - k
                cnt += 1
                break
        else:
            cnt = 0
            break
    print(f'#{t + 1} {cnt}')