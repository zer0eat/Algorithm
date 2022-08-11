# 색칠하기_13630_같은색으로 중첩되어도 확인 가능하게

#input.txt 열기
import sys
sys.stdin = open('input.txt')

#input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    N = int(input()) # 칠할 영역의 수

    # 색칠할 빈 도화지
    white = [[1] * 10 for _ in range(10)]

    #색칠할 영역 input 받기
    for n in range(N):
        # sr = 시작하는 row값 / sc = 시작하는 column 값
        # er = 끝나는 row값 / ec = 끝나는 column 값 / c = 색상
        sr, sc, er, ec, c = map(int, input().split())

        # 빨간색 색칠하기
        if c == 1:
            for i in range(sr, er + 1):
                for j in range(sc, ec + 1):
                    white[i][j] *= 2
        # 파란색 색칠하기
        elif c == 2:
            for i in range(sr, er + 1):
                for j in range(sc, ec + 1):
                    white[i][j] *= 3

    # 보라색 찾기
    purple = 0
    for a in range(10):
        for b in range(10):
            if white[a][b] != 0 and white[a][b] % 6 == 0:
                purple += 1

    print(f'#{t+1} {purple}')
