# 경비원_BOJ2564

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
R, C = map(int, input().split())                                    # 지도의 크기 / R = 행의 길이 / C = 열의 길이
shop_N = int(input())                                               # 상점의 숫자
shop = [list(map(int, input().split())) for n in range(shop_N)]     # 상점의 위치정보 / 0번 인덱스 : 1북쪽, 2남쪽, 3서쪽, 4동쪽 / 1번 인덱스 : 떨어진 거리
Donguen = list(map(int, input().split()))                           # 동근이의 위치정보(상점과 같음)

distance = 0                                                        # 최단거리를 저장할 변수

for s in shop:                                                      # 상점의 위치를 하나씩 확인 할 때

    if Donguen[0] == 1:                                             # 동근이가 북쪽에 있고
        if s[0] == 1:                                               # 상점이 북쪽에 있으면
            distance += abs(s[1]-Donguen[1])                        # 두 거리의 차의 절대 값을 distance에 더한다
        elif s[0] == 2:                                             # 상점이 남쪽에 있으면
            if Donguen[1] + C + s[1] < (R - Donguen[1]) + C + (R - s[1]):   # 시계방향과 반시계방향의 길이를 비교해서 더 짧은 길이를 distance에 더한다
                distance += Donguen[1] + C + s[1]
            elif Donguen[1] + C + s[1] >= (R - Donguen[1]) + C + (R - s[1]):
                distance += (R - Donguen[1]) + C + (R - s[1])
        elif s[0] == 3:                                             # 상점이 서쪽에 있으면
            distance += Donguen[1] + s[1]                           # 반시계 방향으로 돈 거리를 distance에 더한다
        elif s[0] == 4:                                             # 상점이 동쪽에 있으면
            distance += (R - Donguen[1]) + s[1]                     # 시계 방향으로 돈 거리를 distance에 더한다

    elif Donguen[0] == 2:                                           # 동근이가 남쪽에 있고
        if s[0] == 1:                                               # 상점이 북쪽에 있으면
            if Donguen[1] + C + s[1] < (R - Donguen[1]) + C + (R - s[1]):   # 시계방향과 반시계방향의 길이를 비교해서 더 짧은 길이를 distance에 더한다
                distance += Donguen[1] + C + s[1]
            elif Donguen[1] + C + s[1] >= (R - Donguen[1]) + C + (R - s[1]):
                distance += (R - Donguen[1]) + C + (R - s[1])
        elif s[0] == 2:                                             # 상점이 남쪽에 있으면
            distance += abs(s[1] - Donguen[1])                      # 두 거리의 차의 절대 값을 distance에 더한다
        elif s[0] == 3:                                             # 상점이 서쪽에 있으면
            distance += Donguen[1] + (C - s[1])                     # 시계 방향으로 돈 거리를 distance에 더한다
        elif s[0] == 4:                                             # 상점이 동쪽에 있으면
            distance += (R - Donguen[1]) + (C - s[1])               # 반시계 방향으로 돈 거리를 distance에 더한다

    elif Donguen[0] == 3:                                           # 동근이가 서쪽에 있고
        if s[0] == 1:                                               # 상점이 북쪽에 있으면
            distance += Donguen[1] + s[1]                           # 시계 방향으로 돈 거리를 distance에 더한다
        elif s[0] == 2:                                             # 상점이 남쪽에 있으면
            distance += (C- Donguen[1]) + s[1]                      # 반시계 방향으로 돈 거리를 distance에 더한다
        elif s[0] == 3:                                             # 상점이 서쪽에 있으면
            distance += abs(s[1] - Donguen[1])                      # 두 거리의 차의 절대 값을 distance에 더한다
        elif s[0] == 4:                                             # 상점이 동쪽에 있으면
            if Donguen[1] + R + s[1] < (C - Donguen[1]) + R + (C - s[1]):   # 시계방향과 반시계방향의 길이를 비교해서 더 짧은 길이를 distance에 더한다
                distance += Donguen[1] + R + s[1]
            elif Donguen[1] + R + s[1] >= (C - Donguen[1]) + R + (C - s[1]):
                distance += (C - Donguen[1]) + R + (C - s[1])

    elif Donguen[0] == 4:
        if s[0] == 1:                                               # 상점이 북쪽에 있으면
            distance += Donguen[1] + (R - s[1])                     # 반시계 방향으로 돈 거리를 distance에 더한다
        elif s[0] == 2:                                             # 상점이 남쪽에 있으면
            distance += (C - Donguen[1]) + (R - s[1])               # 시계 방향으로 돈 거리를 distance에 더한다
        elif s[0] == 3:                                             # 상점이 서쪽에 있으면
            if Donguen[1] + R + s[1] < (C - Donguen[1]) + R + (C - s[1]):   # 시계방향과 반시계방향의 길이를 비교해서 더 짧은 길이를 distance에 더한다
                distance += Donguen[1] + R + s[1]
            elif Donguen[1] + R + s[1] >= (C - Donguen[1]) + R + (C - s[1]):
                distance += (C - Donguen[1]) + R + (C - s[1])
        elif s[0] == 4:                                             # 상점이 동쪽에 있으면
            distance += abs(s[1] - Donguen[1])                      # 두 거리의 차의 절대 값을 distance에 더한다

print(distance)