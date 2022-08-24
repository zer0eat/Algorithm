# 미로의 거리_13972

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())
for t in range(T):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    # 시작점 찾기
    for i in range(N):  # 미로의 행의 길이 만큼 반복
        for j in range(N):  # 미로의 열의 길이 만큼 반복
            if miro[i][j] == 2:  # 시작점을 찾았다면
                a = i  # 행을 a에 저장
                b = j  # 열을 b에 저장

    stack