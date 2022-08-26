# 파리퇴치_12712

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                                                    # 테스트 케이스
for t in range(T):                                                  # 테스트 케이스만큼 반복할 때
    N, M = map(int, input().split())                                # N = 배열의 길이 / M = 스프레이의 세기
    arr = [list(map(int, input().split())) for _ in range(N)]       # 파리의 영역을 행렬로 저장

    most_kill = 0                                                   # 가장 많이 죽인 파리의 수를 저장할 변수

    # 십자가로 분무할 때
    dx = [-1, 0, 1, 0]                                              # 델타 탐색 행의 위치(상우하좌)
    dy = [0, 1, 0, -1]                                              # 델타 탐색 행의 위치(상우하좌)
    for i in range(N):                                              # 행의 길이 만큼 반복
        for j in range(N):                                          # 열의 길이 만큼 반복
            kill_fly = 0                                            # 십자가 파리킬라로 죽인 파리의 수를 저장할 변수
            for m in range(1, M):                                   # 파리 킬라의 세기만큼 반복하고
                for k in range(4):                                  # 네방향으로 델타탐색으로 이동하여
                    xx = i + (dx[k] * m)                            # 행의 해당 인덱스를 xx로 저장 (i = 중심값 / dx = 상우좌하로 이동한 값 / m = 분무기의 세기)
                    yy = j + (dy[k] * m)                            # 열의 해당 인덱스를 yy로 저장 (j = 중심값 / dy = 상우좌하로 이동한 값 / m = 분무기의 세기)
                    if 0 <= xx <N and 0 <= yy <N:                   # xx와 yy가 행렬을 벗어나지 않을 때
                        kill_fly += arr[xx][yy]                     # 십자가 내의 파리의 수를 kill_fly에 더한 후
            else:                                                   # 십자가 안을 모두 탐색하면
                kill_fly += arr[i][j]                               # 십자가 가운데 파리의 수를 kill_fly에 더해준 후
                if kill_fly > most_kill:                            # most_kill보다 kill_fly이 크다면
                    most_kill = kill_fly                            # most_kill에 kill_fly을 저장

    # X자로 분무할 때
    ddx = [-1, -1, 1, 1]                                            # 델타 탐색 행의 위치(상좌/상우/하우/하좌)
    ddy = [-1, 1, 1, -1]                                            # 델타 탐색 열의 위치(상좌/상우/하우/하좌)
    for i in range(N):                                              # 행의 길이 만큼 반복
        for j in range(N):                                          # 열의 길이 만큼 반복
            kill_fly = 0                                            # x자 파리킬라로 죽인 파리의 수를 저장할 변수
            for m in range(1, M):                                   # 파리 킬라의 세기만큼 반복하고
                for k in range(4):                                  # 네방향으로 델타탐색으로 이동하여
                    xxx = i + (ddx[k] * m)                          # 행의 해당 인덱스를 xxx로 저장 (i = 중심값 / ddx = 상좌/상우/하우/하좌로 이동한 값 / m = 분무기의 세기)
                    yyy = j + (ddy[k] * m)                          # 열의 해당 인덱스를 yyy로 저장 (j = 중심값 / ddy = 상좌/상우/하우/하좌로 이동한 값 / m = 분무기의 세기)
                    if 0 <= xxx < N and 0 <= yyy < N:               # xxx와 yyy가 행렬을 벗어나지 않을 때
                        kill_fly += arr[xxx][yyy]                   # X자 내의 파리의 수를 kill_fly에 더한 후
            else:                                                   # X자 안을 모두 탐색하면
                kill_fly += arr[i][j]                               # X자 가운데 파리의 수를 kill_fly에 더해준 후
                if kill_fly > most_kill:                            # most_kill보다 kill_fly이 크다면
                    most_kill = kill_fly                            # most_kill에 kill_fly을 저장

    print(f'#{t+1}', most_kill)
