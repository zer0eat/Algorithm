# 유기농배추_BOJ1012

# input.txt
import sys
sys.stdin = open('input.txt')

def worm(i, j):                                         # 지렁이가 지킬수 있는 범위를 찾을 함수
    baechu[i][j] = 2                                    # 현재 위치를 2로 표시하고
    for u in range(4):                                  # 델타탐색해서
        if 0 <= i+dx[u] < N and 0 <= j+dy[u] < M:       # 밭의 범위 안이라면
            if baechu[i+dx[u]][j+dy[u]] == 1:           # 배추가 심어져 있는 곳이라면
                worm(i+dx[u], j+dy[u])                  # worm 함수를 돌려 지킬수 있는 범위를 늘린다

# input 받기
T = int(sys.stdin.readline())                           # 테스트 케이스
for t in range(T):                                      # 테스트 케이스를 반복해서
    M, N, K = map(int,sys.stdin.readline().split())     # M 가로의길이 / N 세로의길이 / K 배추의 개수
    baechu = [[0]*M for _ in range(N)]                  # 배추를 심을 빈 밭을 리스트로 생성

    for k in range(K):                                  # 배추의 수만큼 반복해서
        a, b = map(int,sys.stdin.readline().split())    # 배추의 좌표를 받은 후
        baechu[b][a] = 1                                # 배추를 밭에 1로 표시한다

    dx = [-1,0,1,0]                                     # 델타탐색을 위한 행(상우하좌)리스트
    dy = [0,1,0,-1]                                     # 델타탐색을 위한 열(상우하좌)리스트

    cnt = 0                                             # 지렁이의 수를 저장할 변수
    for i in range(N):                                  # 행을 반복하고
        for j in range(M):                              # 열을 반복해서
            if baechu[i][j] == 1:                       # 배추가 표시되어 있다면
                worm(i, j)                              # 지렁이를 풀어 지렁이가 지킬수 있는 범위를 표시한다
                cnt += 1                                # 지렁이의 마리수를 1 추가한다
    else:                                               # 반복을 마치면 지렁이의 수를 출력한다
        print(cnt)