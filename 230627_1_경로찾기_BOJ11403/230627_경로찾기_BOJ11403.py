# 경로찾기_BOJ11403

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())                                                # 정점의 개수를 input 받고
lst = [list(map(int, input().split())) for _ in range(N)]       # 그래프의 인접행렬을 리스트 형태로 input 받는다
for i in range(N):                                              # 정점의 개수를 반복해서
    visited = [0] * N                                           # 갈 수 있는 정점을 표시할 리스트를 생성하고
    tmp = deque([i])                                            # 갈 수 있는 정점을 탐색할 deque를 생성한다
    while tmp:                                                  # tmp가 빌때까지 반복해서
        a = tmp.popleft()                                       # tmp에서 갈 수 있는 점을 pop해서
        for j in range(N):                                      # a 점에서 갈 수 있는 정점을 반복한다
            if lst[a][j] == 1:                                  # a 점에서 갈 수 있는 정점이 나왔다면
                if visited[j] == 0:                             # 해당 정점이 방문 전일 경우에
                    visited[j] = 1                              # 방문 표시를 한 후
                    tmp.append(j)                               # tmp에 append 한다
    else:                                                       # while문을 마쳤다면
        print(*visited)                                         # i 번째 줄에서 갈 수 있는 줄을 출력한다