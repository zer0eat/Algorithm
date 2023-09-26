# 데스 나이트_BOJ16948

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                                        # 체스판의 길이를 input 받고
r1, c1, r2, c2 = map(int, input().split())              # 시작점의 위치와 도착점의 위치를 input 받는다
knight = [[-2,-1],[-2,1],[0,-2],[0,2],[2,-1],[2,1]]     # 나이트가 이동할 수 있는 곳을 리스트로 생성하고
visited = [[0]*N for _ in range(N)]                     # 방문표시를 할 행렬을 생성한다
visited[r1][c1] = 1                                     # 시작점을 방문표시하고
lst = [[0, [r1, c1]]]                                   # 시작점의 이동횟수와 위치를 넣은 리스트를 생성한다
while lst:                                              # lst가 빌때까지 반복해서
    cnt, now = heapq.heappop(lst)                       # 이동횟수와 이동위치를 heappop한다
    if now == [r2, c2]:                                 # 도착지에 도착한 경우
        print(cnt)                                      # 최소 이동 횟수를 출력하고
        break                                           # while문을 break한다
    for t in range(6):                                  # 나이트의 이동범위를 반복해서
        x = now[0] + knight[t][0]                       # 이동한 곳의 행을 x에 저장하고
        y = now[1] + knight[t][1]                       # 이동한 곳의 열을 y에 저장한다
        if 0<=x<N and 0<=y<N:                           # 이동한 곳이 체스판 내에 있고
            if visited[x][y] == 0:                      # 아직 방문 전이라면
                visited[x][y] = 1                       # 방문표시를 하고
                heapq.heappush(lst, [cnt+1, [x,y]])     # lst에 이동횟수와 이동위치를 heappush한다
else:                                                   # 도착지로 이동할 수 없는 경우
    print(-1)                                           # -1을 출력한다