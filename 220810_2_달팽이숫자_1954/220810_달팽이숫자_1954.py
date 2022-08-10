# 달팽이숫자_1954

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())
for t in range(T):
    N = int(input())

    # 달팽이가 지나갈 행렬 만들기
    snail = [[0]*N for _ in range(N)]

    # 달팽이가 지나가는 조건 설정
    row = 0 # 달팽이의 row 값
    col = -1 # 달팽이의 col 값
    cnt = 1 # 입력할 값
    M = 2*N # 달팽이가 이동하면서 소모할 값(2N-1만큼 가로 세로로 이동)
    T = 2*N # 달팽이가 몇 번 이동할지 기준이 될 값

    # 달팽이가 지나가면서 cnt만큼 값을 저장장
   while M > 1:
        if T == M: # 왼쪽으로 오른쪽으로 이동하는 첫 이동
            for i in range(N):
                col += 1
                snail[row][col] = cnt
                cnt += 1
            else:
                M -= 1
                N -= 1
        elif M > 1:
            if (T - M) % 4 == 1: #위에서 아래로 이동
                for a in range(N):
                    row += 1
                    snail[row][col] = cnt
                    cnt += 1
                else:
                    M -= 1
            elif (T - M) % 4 == 2: #오른쪽에서 왼쪽으로 이동
                for a in range(N):
                    col -= 1
                    snail[row][col] = cnt
                    cnt += 1
                else:
                    M -= 1
                    N -= 1
            elif (T - M) % 4 == 3: #아래에서 위로 이동
                for a in range(N):
                    row -= 1
                    snail[row][col] = cnt
                    cnt += 1
                else:
                    M -= 1
            elif (T - M) % 4 == 0: #왼쪽에서 오른쪽으로 이동
                for a in range(N):
                    col += 1
                    snail[row][col] = cnt
                    cnt += 1
                else:
                    M -= 1
                    N -= 1

    print(f'#{t+1}')
    for i in snail:
        print(*i)









