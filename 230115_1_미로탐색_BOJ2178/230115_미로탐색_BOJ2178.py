# 미로탐색_BOJ2178

# input.txt 열기
import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')

def BFS(tmp):
    global num                                                  # num을 global로 불러오고
    A = []                                                      # A 리스트를 생성한다
    num += 1                                                    # num을 1 증가 시킨 후
    while tmp:                                                  # tmp가 빌때까지 반복한다
        Z = tmp.pop()                                           # tmp에서 요소를 pop해서 Z에 저장하고
        for i in range(4):                                      # Z위치에서 상우하좌 델타탐색을 위한 반복을 하고
            if 0 <= Z[0]+dx[i] < N and 0 <= Z[1]+dy[i] < M:     # 델타탐색의 위치가 행렬 내에 있고
                if miro[Z[0]+dx[i]][Z[1]+dy[i]] == '1':         # 델타탐색의 원소가 '1'이라면
                    A.append([Z[0]+dx[i], Z[1]+dy[i]])          # A에 좌표를 append하고
                    miro[Z[0] + dx[i]][Z[1] + dy[i]] = num      # 좌표의 원소를 num으로 바꾼다
    else:                                                       # while문의 반복이 끝나면
        if A:                                                   # A가 비어있는 리스트가 아니라면
            BFS(A)                                              # BFS로 A에 담겨있는 좌표를 탐색한다

# input 받기
N, M = map(int, sys.stdin.readline().split())                   # N 행의길이 / M 열의길이
miro = [list(sys.stdin.readline().strip()) for _ in range(N)]   # miro를 행렬로 input 받기
dx = [-1, 0, 1, 0]                                              # 델타탐색을 위한 행을 이동을 리스트로 생성
dy = [0, 1, 0, -1]                                              # 델타탐색을 위한 열의 이동을 리스트로 생성
num = 1                                                         # BFS의 깊이를 적기 위한

tmp = [[0, 0]]                                                  # tmp 리스트에 시작점인 0,0을 넣고
BFS(tmp)                                                        # BFS로 탐색한다
print(miro[N-1][M-1])                                           # 도착지인 N-1, M-1을 출력한다