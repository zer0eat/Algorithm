# 파이프 옮기기 1_BOJ17070

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())                                                                # 집의 크기를 input 받고
lst = [list(map(int, input().split())) for _ in range(N)]                       # 집의 상태를 input 받은 후
cnt = 0                                                                         # 파이프를 이동시키는 방법의 수를 저장할 변수를 생성하고

def dfs(pipe, r, c):
    global cnt                                                                  # 방법의 수를 저장할 cnt를 global 변수로 선언하고
    if r == N-1 and c == N-1:                                                   # 행과 열이 모두 N에 도달했다면
        cnt += 1                                                                # 방법의 수를 1 추가하고
    else:                                                                       # 행 또는 열이 N에 도착하지 못했다면
        if r+1 < N and c+1 < N:                                                 # 대각선으로 이동한 곳이 집 안이면서
            if lst[r+1][c] == 0 and lst[r][c+1] == 0 and lst[r+1][c+1] == 0:    # 아래 / 오른쪽 / 대각선 아래 모두 벽이 아니라면
                dfs(1, r+1, c+1)                                                # 대각선으로 이동시킨 파이프를 dfs로 탐색한다
        if (pipe == 0 or pipe == 1) and c+1 < N:                                # 파이프가 가로 또는 대각선으로 놓인 상태면서 가로로 이동한 곳이 집 안이라면
            if lst[r][c+1] == 0:                                                # 오른쪽이 벽이 아니라면
                dfs(0, r, c+1)                                                  # 가로로 이동시킨 파이프를 dfs로 탐색한다
        if (pipe == 1 or pipe == 2) and r+1 < N:                                # 파이프가 세로 또는 대각선으로 놓인 상태면서 세로로 이동한 곳이 집 안이라면
            if lst[r+1][c] == 0:                                                # 아래쪽이 벽이 아니라면
                dfs(2, r+1, c)                                                  # 세로로 이동시킨 파이프를 dfs로 탐색한다

dfs(0,0,1)                                                                      # 가로로 놓인 파이프를 시작으로 dfs 탐색을 한다
print(cnt)                                                                      # 파이프를 이동시키는 방법의 수를 출력한다