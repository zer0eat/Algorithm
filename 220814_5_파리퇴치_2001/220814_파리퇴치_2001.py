# 파리퇴치_2001

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    N, K = input().split()
    N = int(N) # 파리가 존재하는 행렬의 크기
    K = int(K) # 파리채 행렬의 크기
    fly_field = [list(map(int, input().split())) for _ in range(N)] # 파리가 존재하는 행렬

    # 파리채 영역에서 가장 많은 수의 파리가 존재하는 곳 구하기
    max_fly = 0
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            # 파리채의 영역 내 파리의 합 구하기
            flapper = 0
            for k in range(K):
                for k2 in range(K):
                    flapper += fly_field[i+k][j+k2]
            # flapper 내의 파리의 수가 max_fly 보다 크면 숫자 교체
            if flapper > max_fly:
                max_fly = flapper

    print(f'#{t+1}', max_fly)


