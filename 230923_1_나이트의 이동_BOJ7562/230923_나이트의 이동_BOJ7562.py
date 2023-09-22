# 나이트의 이동_BOJ7562

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
T = int(input())                                                        # 테스트케이스를 input받고
knight = [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]      # 나이트가 이동할 수 있는 지점을 리스트로 생성한다
for t in range(T):                                                      # 테스트 케이스를 반복해서
    N = int(input())                                                    # 체스판의 길이를 input 받고
    visited = [[0]*N for _ in range(N)]                                 # 방문표시를 할 행렬을 생성한다
    start = list(map(int, input().split()))                             # 시작지점을 input 받고
    end = list(map(int, input().split()))                               # 도착지점을 input 받는다
    bfs = [[0, start]]                                                  # 이동횟수와 시작지점을 리스트에 넣고 생성한 후
    visited[start[0]][start[1]] = 1                                     # 시작지점을 방문표시를 한다
    while bfs:                                                          # bfs가 빌 때까지 반복해서
        cnt, K = heapq.heappop(bfs)                                     # 이동횟수와 이동지점을 bfs에서 heappop해서
        if K == end:                                                    # 이동지점이 도착지점이라면
            print(cnt)                                                  # 이동횟수를 출력하고
            break                                                       # while문을 break한다
        for i in range(8):                                              # 나이트가 이동할 8방향을 반복해서
            x = K[0] + knight[i][0]                                     # 이동한 행의 좌표와
            y = K[1] + knight[i][1]                                     # 이동한 열의 좌표를 저장하고
            if 0<=x<N and 0<=y<N and visited[x][y] == 0:                # 이동한 곳이 체스판 안이고 방문 전이라면
                heapq.heappush(bfs, [cnt+1, [x, y]])                    # bfs에 이동횟수에 1을 추가하고 이동지점을 리스트에 담아 heappush하고
                visited[x][y] = 1                                       # 이동한 곳을 방문표시한다