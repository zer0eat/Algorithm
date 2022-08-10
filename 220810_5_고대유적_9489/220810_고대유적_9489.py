# 고대유적_9489

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_l = 0
    # 가로줄의 최대 값
    for i in range(N):
        leng = 0
        for j in range(M):
            if arr[i][j] == 1:
                leng += 1
                if leng > max_l:
                    max_l = leng
            elif arr[i][j] == 0:
                leng = 0

    max_k = 0
    # 세로줄의 최대 값
    for j in range(M):
        leng = 0
        for i in range(N):
            if arr[i][j] == 1:
                leng += 1
                if leng > max_k:
                    max_k = leng
            elif arr[i][j] == 0:
                leng = 0

    # 가로 세로 중 최대 값 인쇄
    if max_l > max_k:
        print(f'#{t+1} {max_l}')
    else:
        print(f'#{t+1} {max_k}')
