# ladder1_1210

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = 10
for t in range(T):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 사다리 타기
    up = 99
    for l in range(100):
        side = 0
        # 당첨 자리 찾기
        if ladder[99][l] == 2:
            up -= 1
            side = l

            # 당첨 자리부터 위로 사다리 타기
            while up > -1:

                # 맨 오른쪽 줄일때
                if side == 99:
                    # 왼쪽에 1이 없으면 위로 이동
                    if ladder[up-1][side] == 1 and ladder[up][side-1] == 0:
                        up -= 1
                    # 왼쪽에 1이 있으면 1이 끝날 때까지 이등 후 한칸 위로
                    elif ladder[up-1][side] == 1 and ladder[up][side-1] == 1:
                        while ladder[up][side-1] == 1:
                            side -= 1
                        else:
                            up -= 1

                # 맨 왼쪽 줄일때
                elif side == 0:
                    # 오른쪽에 1이 없으면 위로 이동
                    if ladder[up-1][side] == 1 and ladder[up][side+1] == 0:
                        up -= 1
                    # 오른쪽에 1이 있으면 끝날 때까지 이동 후 한칸 위로
                    elif ladder[up-1][side] == 1 and ladder[up][side+1] == 1:
                        while ladder[up][side+1] == 1:
                            side += 1
                        else:
                            up -= 1

                # 사이의 줄일때
                elif side in range(1, 99):
                    # 양 옆에 1이 없으면 위로 한칸 이동
                    if ladder[up-1][side] == 1 and ladder[up][side-1] == 0 and ladder[up][side+1] == 0:
                        up -= 1
                    # 오른쪽에 1이 있으면 끝날때 까지 이동 후 위로 한칸 이동
                    elif ladder[up-1][side] == 1 and ladder[up][side+1] == 1:
                        while side != 99 and ladder[up][side + 1] == 1:
                            side += 1
                        else:
                            up -= 1
                    # 왼쪽에 1이 있으면 끝날때 까지 이동 후 위로 한칸 이동
                    elif ladder[up-1][side] == 1 and ladder[up][side-1] == 1:
                        while ladder[up][side - 1] == 1 and side != 0:
                            side -= 1
                        else:
                            up -= 1
            print(f'#{t+1} {side}')


